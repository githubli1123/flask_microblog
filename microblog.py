# -*- coding = utf-8 -*-
# @Time  : 2021/10/21 17:19
# @Author : ZhouJie Wu
# @File  : .py
# @Software:PyCharm
from app import app
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
# 在处理应用程序时，经常需要在Python shell中进行测试，如果每次都要重复上述导入，将变得极其乏味、麻烦。
# flask shell命令是flask命令伞中另一个非常有用的工具。shell命令是在run之后，Flask执行的第二个核心命令。
# 这个命令的目的是在应用程序的上下文中启动Python解释器


if __name__ == '__main__':
    app.run(debug=True)




