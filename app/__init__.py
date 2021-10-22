# -*- coding = utf-8 -*-
# @Time  : 2021/10/21 17:04
# @Author : ZhouJie Wu
# @File  : .py
# @Software:PyCharm
from flask import Flask    # 从flask包中导入Flask类

app = Flask(__name__)   # 将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
# print('等会谁（哪个包或模块）在使用我：', __name__)

from app import routes   # 从app包中导入模块routes
# 注：上面两个app是完全不同的东西。两者都是纯粹约定俗成的命名，可重命名其他内容。
# 奇怪:该行代码放到第七行会报错?






