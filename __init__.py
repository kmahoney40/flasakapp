from flask import Flask,jsonify,request
import logging
from logging.handlers import RotatingFileHandler
#from logging import FileHandler, WARNING
import json

app = Flask(__name__)

#handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
#handler.setLevel(logging.INFO)
#app.logger.addHandler(handler)
    
@app.route("/")
@app.route("/woot")
def hello():
    ret_val = jsonify(
        {'val':"Logo and disclaimer"}
    )
    app.logger.warning('A warning occurred (%d apples)', 42)
    r = ret_val#{ "item":  "Logo and Disclaimer"}

    return r
 
@app.route("/test")
def test():
    #return "success"
    ret_val = jsonify(
        val="Logo and disclaimer"
    )
    app.logger.warning('A warning from /test (%d apples)', 42)
    r = ret_val#{ "item":  "Logo and Disclaimer"}
    return r
 
@app.route("/pi")
def pi():
    return "https://www.raspberypi.org"

@app.route("/post1", methods=['GET','POST'])
def post1():
    app.logger.warning('A warning from /post1 (%s apples)', request.json['item'])
    #ret_val = jsonify(
    #    item='JSON ITEM',
    #    I2='TWO'
    #)
    app.logger.warning('json.dumps (%s apples)', json.dumps(request.json))
    #app.logger.warning('json.dumps2 (%s apples)', json.dumps(ret_val))
    r = request.json['item']
    return r

if __name__ == "__main__":
    #handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    #handler.setLevel(logging.INFO)
    #app.logger.addHandler(handler)

    app.run(host='0.0.0.0',debug=True)
