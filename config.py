# -*- coding = utf-8 -*-
# @Time  : 2021/10/23 17:09
# @Author : ZhouJie Wu
# @File  : .py
# @Software:PyCharm

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'


