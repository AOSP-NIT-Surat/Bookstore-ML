from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
s = os.environ.get("DATABASE_URL")
s = 'postgresql+psycopg2:/' + s[s.find('/')+1:]
app.config['SQLALCHEMY_DATABASE_URI'] = s
db = SQLAlchemy(app)

from db.tables import user

@app.route("/prediction", methods=["POST"])
def prediction():
    return

@app.route("/image_ocr", methods=["POST"])
def ocr_enable():
    return

@app.route("/login", methods=["POST"])
def login():
    username = request.json["Username"]
    password = request.json["Password"]
    return dict({"Successful":user.User.login_user(username,password)})