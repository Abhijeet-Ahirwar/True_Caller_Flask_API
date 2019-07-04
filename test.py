from flask_pymongo import PyMongo
from flask import Flask,jsonify,request
import os

app=Flask(__name__)


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/detail"
mongo = PyMongo(app)
# @app.route("/")
# def home_page():
#     online_users = mongo.User_data.find()
#     return online_users

lang={'name': 'Zara','Age':23}
@app.route('/',methods=['GET'])
def hello():
	add=mongo.db.col
	t=[]
	for a in add.find():
		t.append(a)
	return str(t)
# @app.route('/lan',methods=['GET'])
# def retur():
# 	return jsonify({'languages':lang})

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT',2010))
    app.run(host=host, port=port)
