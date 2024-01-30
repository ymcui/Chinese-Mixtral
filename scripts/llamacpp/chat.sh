#!/bin/bash

# script to chat with Chinese-Mixtral-Instruct model
# usage: ./chat.sh chinese-mixtral-instruct-gguf-model-path
# WARNING: the hyperparameters are not optimal, please tune them yourself

./main -m $1 --color --interactive-first \
-c 4096 -t 6 --temp 0.2 --repeat_penalty 1.1 -ngl 999 \
--in-prefix ' [INST] ' --in-suffix ' [/INST]'