# 构造文件，包含程序实例
# 启动程序时，首先执行的是该文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask('theboard')
app.config.from_pyfile('settings.py')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
moment = Moment(app)

from theboard import errors, views, commands

