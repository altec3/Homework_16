from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("../configs/flask_config.py")
db = SQLAlchemy(app)
