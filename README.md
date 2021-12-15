# japanese-dialog-transformers

このレポジトリはNTTより公開されている[the Japanese Transformer Encoder-decoder dialogue model](https://github.com/nttcslab/japanese-dialog-transformers) について，APIを経由することでシステムと簡単に対話を行えるようにするためのコードを公開しています．このレポジトリに含まれるコードのうち，[scripts/dialog_flask.py](scripts/dialog_flask.py)は，NTTが公開しているレポジトリの[dialog.py](https://github.com/nttcslab/japanese-dialog-transformers/blob/main/scripts/dialog.py)に基づきます．


## Update log

* Dec. 16, 2022: published

---

## How to use  

### Install dependent libraries  
- Python 3.7.10
- CUDA 11.1/10.2  
- Pytorch 1.8.2  
- fairseq 1.0.0a0（githubから飲み利用できるバージョン）  
- sentencepiece 0.1.96  

### Quick start

1. `$ pip install -m requirements.txt`でライブラリをインストールしてください．    
2. その他必要なファイルをNTTのリポジトリからダウンロードしてください．  
3. `$ sh flask-fairseq.sh`でローカルサーバを立ち上げてください（デフォルトはポート番号5000で立ち上がります）．  
4. json形式のデータ`{"message":<送りたい発話>}`をhttp://localhost:5000/get_response`にGETリクエストで送ると，システムからの応答がjson形式で返ってきます．  

### flask-fairseq
利用できるパラメータはfairseqと同じです．

~~~
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
~~~