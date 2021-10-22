# -*- coding = utf-8 -*-
# @Time  : 2021/10/21 17:16
# @Author : ZhouJie Wu
# @File  : .py
# @Software:PyCharm

from app import app  # 从app包中导入 app 这个实例

# 2个路由
@app.route('/')
@app.route('/index')
# 1个视图函数
def index():
	return "Hello,World!"   # 返回一个字符串






