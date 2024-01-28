#!/bin/bash

# script to chat with Chinese-Mixtral-Instruct model
# usage: ./chat.sh chinese-mixtral-instruct-gguf-model-path your-first-instruction

MODEL_PATH=$1
FIRST_INSTRUCTION=$2

./main -m $MODEL_PATH \
-c 4096 -t 6 --temp 0.5 --repeat_penalty 1.1 -ngl 999 \
--color -i $HPARAMS --in-prefix ' [INST] ' --in-suffix ' [/INST]' \
-p "[INST] $FIRST_INSTRUCTION [/INST]" 