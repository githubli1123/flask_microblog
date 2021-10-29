# -*- coding = utf-8 -*-
# @Time  : 2021/10/27 9:02
# @Author : ZhouJie Wu
# @File  : .py
# @Software:PyCharm
from app import db
from datetime import datetime


class User(db.Model):       # 创建的User类继承自db.Model，它是Flask-SQLAlchemy所有模型的基类
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')   # 不理解？？？？？？

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # db.ForeignKey()中，模型由数据库表名称给出，SQLAlchemy自动使用小写字符，对于多字模型名称将使用“snake case”命名约定

    def __repr__(self):
        return '<Post {}>'.format(self.body)








