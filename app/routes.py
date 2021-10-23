# -*- coding = utf-8 -*-
# @Time  : 2021/10/21 17:16
# @Author : ZhouJie Wu
# @File  : .py
# @Software:PyCharm
from app import app  # 从app包中导入 app 这个实例
from flask import render_template, flash, url_for
from app.forms import LoginForm
from werkzeug.utils import redirect


# 2个路由
@app.route('/')
@app.route('/index')
# 1个视图函数
def index():
	# user = {'username': 'ZhouJie Wu'}
	# return render_template('index.html', title='Home', user=user)    # 返回一个字符串
	user = {'username': 'Miguel'}  # 用户
	posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])     # method
def login():
	form = LoginForm()   # 表单实例化对象
	if form.validate_on_submit():
		flash('Login requested for user {},remember_me={}'.format(form.username.data, form.remember_me.data))  # 前端显示字符串
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)






