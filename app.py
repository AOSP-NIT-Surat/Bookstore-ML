from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
database_url = os.environ.get("DATABASE_URL")
database_url = 'postgresql+psycopg2:/' + database_url[database_url.find('/')+1:]
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
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