import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_wtf import CSRFProtect  # 导入csrf 保护
from flask_restful import Api

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_pyfile("settings.py")
app.config.from_object("settings.Config")  # 来源于类对象
app.secret_key = "123123"
models = SQLAlchemy(app)
csrf = CSRFProtect(app)  # 使用csrf保护
api = Api(app)
