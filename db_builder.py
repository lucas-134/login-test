from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "test.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wgyeafjhgkrsldbhreagkndl'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

with app.app_context():
  db.create_all()

