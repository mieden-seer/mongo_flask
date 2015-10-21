from datetime import datetime
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import g
from flask import url_for
from flask import flash

mod = Blueprint('default', __name__)

@mod.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('default/index.html', server_time=current_time)

@mod.route('/login', methods=['GET'])
def login_page():
    return render_template('default/login.html')

@mod.route('/login', methods=['POST'])
def login_submit():
	g.usersdb.getUser(request.form['username'], request.form['password'])
	return redirect('/posts/')