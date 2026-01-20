from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.sqlite'

db = SQLAlchemy(app)

# ❌ คอมเมนต์ไว้ก่อน
# from epl import routes, models
