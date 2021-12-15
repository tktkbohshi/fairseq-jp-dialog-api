# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify
from fairseq.dataclass.utils import convert_namespace_to_omegaconf
from fairseq import options
from dialog_flask import FavotModel, Favot, add_local_args

print("# Load fairseq configurations and a model")
# fairseq configuration
parser = options.get_interactive_generation_parser()
add_local_args(parser)
args = options.parse_args_and_arch(parser)
cfg = convert_namespace_to_omegaconf(args)
fm = FavotModel(args)
favot = Favot(args, fm, parser=parser)

print("# Load flask configuration")
# flask configuration
app = Flask(__name__)
# Countermeasures against garbled text
app.config['JSON_AS_ASCII']=False

#--------------------------------------------------------API--------------------------------------------------------
# curl -XGET -d '{"message":"Hello!"}' -H "Content-Type: application/json" http://localhost:5000/get_response
@app.route("/get_response", methods=["GET"])
def return_message():
    arg = request.get_json()
    print(arg)
    received_message = arg["message"]
    ret = favot.execute(received_message.rstrip("\n"))

    if ret is None or len(ret) != 2:
        return jsonify({'response': arg["message"]})
    ret, ret_debug = ret
    if ret is not None:
        return jsonify({'response': ret})
    

if __name__ == '__main__':
  app.run(host=os.getenv('APP_ADDRESS', 'localhost'), port=5000, debug=True)