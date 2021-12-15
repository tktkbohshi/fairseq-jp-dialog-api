#!/bin/bash
python scripts/flask_main.py ${DATA_PATH} \
 --path ${MODEL_PATH} \
 --min-len 10 \
 --source-lang src \
 --target-lang dst \
 --tokenizer space \
 --bpe sentencepiece \
 --sentencepiece-model data/dicts/sp_oall_32k.model \
 --no-repeat-ngram-size 3 \
 --beam 10 \
 --sampling \
 --nbest 10 \
 --sampling-topp 0.9 \
 --temperature 1.0 \
 --show-nbest 1