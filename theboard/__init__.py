# 构造文件，包含程序实例
# 启动程序时，首先执行的是该文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('theboard')
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)

from theboard import errors, views, commands

