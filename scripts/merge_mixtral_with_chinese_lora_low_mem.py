"""
Usage: 
python merge_mixtral_with_chinese_lora_low_mem.py \
    --base_model path/to/Mixtral-8x7B-v0.1 \
    --lora_model path/to/chinese-Mixtral-8x7B-v0.1-lora \
    --output_dir path/to/output-dir
"""
import argparse
import json
import os
import gc
import torch
import peft
from transformers import LlamaTokenizer
from transformers.modeling_utils import dtype_byte_size
from huggingface_hub import snapshot_download
import re
import safetensors
from safetensors.torch import load_file as safe_load_file


parser = argparse.ArgumentParser(description='Script to merge Mixtral-8x7B-v0.1 with Chinese-Mixtral-LoRA weights')
parser.add_argument('--base_model', default=None, required=True,
                    type=str, help="Base model path (basically Mixtral-8x7B-v0.1)")
parser.add_argument('--lora_model', default=None, required=True,
                    type=str, help="LoRA model path (Chinese-Mixtral-LoRA, Chinese-Mixtral-Instruct-LoRA)")
parser.add_argument('--output_dir', default='./merged_model',
                    type=str, help="Output path for the merged model")
parser.add_argument('--verbose', default=False, action='store_true',
                    help="Show detailed debugging messages")

WEIGHTS_NAME = "adapter_model.bin"
SAFETENSORS_WEIGHTS_NAME = "adapter_model.safetensors"


def transpose(weight, fan_in_fan_out):
    return weight.T if fan_in_fan_out else weight


def jsonload(filename):
    with open(filename, "r") as file:
        d = json.load(file)
    return d


if __name__=='__main__':
    args = parser.parse_args()
    base_model_path = args.base_model
    lora_model_path = args.lora_model
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    print(f"="*80)
    print(f"Base model: {base_model_path}")
    print(f"LoRA model: {lora_model_path}")

    tokenizers_and_loras = []
    print(f"Loading {lora_model_path}")
    if not os.path.exists(lora_model_path):
        print("Cannot find lora model on the disk. Downloading lora model from hub...")
        lora_model_path = snapshot_download(repo_id=lora_model_path)
    tokenizer = LlamaTokenizer.from_pretrained(lora_model_path, legacy=True)
    lora_config = peft.LoraConfig.from_pretrained(lora_model_path)
    if os.path.exists(os.path.join(lora_model_path, SAFETENSORS_WEIGHTS_NAME)):
        lora_filename = os.path.join(lora_model_path, SAFETENSORS_WEIGHTS_NAME)
        use_safetensors = True
    elif os.path.exists(os.path.join(lora_model_path, WEIGHTS_NAME)):
        lora_filename = os.path.join(lora_model_path, WEIGHTS_NAME)
        use_safetensors = False
    else:
        raise ValueError(
                    f"Please check that the file {WEIGHTS_NAME} or {SAFETENSORS_WEIGHTS_NAME} is present at {lora_model_path}."
                )
    if use_safetensors:
        lora_state_dict = safe_load_file(lora_filename, device="cpu")
    else:
        lora_state_dict = torch.load(lora_filename, map_location='cpu')
    if 'base_model.model.model.embed_tokens.weight' in lora_state_dict:
        lora_vocab_size = lora_state_dict['base_model.model.model.embed_tokens.weight'].shape[0]
        assert lora_vocab_size == len(tokenizer), \
        (f"The vocab size of the tokenizer {len(tokenizer)} does not match the vocab size of the LoRA weight {lora_vocab_size}!\n")
    tokenizers_and_loras.append(
        {
            "tokenizer"  :tokenizer,
            "state_dict" :lora_state_dict,
            "config": lora_config,
            "scaling": lora_config.lora_alpha / lora_config.r,
            "fan_in_fan_out" : lora_config.fan_in_fan_out,
        })

    if not os.path.exists(base_model_path):
        print("Cannot find lora model on the disk. Downloading lora model from hub...")
        base_model_path = snapshot_download(repo_id=base_model_path)
    ckpt_filenames = sorted([f for f in os.listdir(base_model_path) if re.match(r'model-(\d+)-of-(\d+).safetensors',f)])
    if len(ckpt_filenames) == 0:
        raise FileNotFoundError(f"Cannot find base model checkpoints in ${base_model_path}. Please make sure the checkpoints are saved in the HF format.")
    total_size = 0
    for index, filename in enumerate(ckpt_filenames):
        print(f"Loading ckpt {filename}")
        if re.match('(.*).safetensors', filename):
            state_dict = safe_load_file(os.path.join(base_model_path,filename), device="cpu")
        else:
            state_dict = torch.load(os.path.join(base_model_path,filename), map_location='cpu')
        print("Merging...")
        for k in state_dict:
            for tl_idx, t_and_l in enumerate(tokenizers_and_loras):
                saved_key = 'base_model.model.'+k
                lora_key_a = saved_key.replace('.weight','.lora_A.weight')
                if saved_key in t_and_l['state_dict']:
                    if args.verbose:
                        print(f"copying {saved_key} from {tl_idx}-th LoRA weight to {k}")
                    state_dict[k] = t_and_l['state_dict'][saved_key].half().clone() # do we need half()?
                if lora_key_a in t_and_l['state_dict']:
                    lora_key_b = lora_key_a.replace('lora_A.weight','lora_B.weight')
                    if args.verbose:
                        print(f"merging {lora_key_a} and lora_B.weight form {tl_idx}-th LoRA weight to {k}")
                    state_dict[k] += (
                        transpose(
                            t_and_l['state_dict'][lora_key_b].float() @ t_and_l['state_dict'][lora_key_a].float(), t_and_l['fan_in_fan_out']) * t_and_l['scaling']
                    )
            weight_size = state_dict[k].numel() * dtype_byte_size(state_dict[k].dtype)
            total_size += weight_size

        print(f"Saving ckpt {filename} to {output_dir} in HF format...")
        if use_safetensors:
            safetensors.torch.save_file(
                        state_dict, os.path.join(output_dir, filename), metadata={"format": "pt"}
                    )
        else:
            torch.save(state_dict, os.path.join(output_dir, filename))
        del state_dict
        gc.collect()    # Effectively enforce garbage collection

    print(f"Saving tokenizer")
    tokenizers_and_loras[-1]['tokenizer'].save_pretrained(output_dir)

    configs = ('config.json', 'generation_config.json', "model.safetensors.index.json")
    for config in configs:
        if os.path.exists(os.path.join(lora_model_path, config)):
            print(f"Saving {config} from {lora_model_path}")
            with open(os.path.join(lora_model_path, config),'r') as f:
                obj = json.load(f)
        else:
            if os.path.exists(os.path.join(base_model_path, config)):
                print(f"Saving {config} from {base_model_path}")
                with open(os.path.join(base_model_path, config),'r') as f:
                    obj = json.load(f)
                if config == 'config.json':
                    obj['vocab_size'] = len(tokenizers_and_loras[-1]['tokenizer'])
                if config == "model.safetensors.index.json":
                    obj['metadata']['total_size'] = total_size
        if os.path.exists(os.path.join(base_model_path, config)):
            with open(os.path.join(output_dir, config), 'w') as f:
                json.dump(obj, f, indent=2)
    print("Done.")
    print(f"Check output dir: {output_dir}")