from flask import Blueprint
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

ur = Blueprint('users', __name__)

@ur.route('/signup', methods=['GET'])
def signup_page():
	return render_template('users/signup.html')

@ur.route('/signup', methods=['POST'])
def signup_submit():
	username = request.form['username']
	password = request.form['password']

	print username

	g.usersdb.signupUser(username, password)

	return redirect(url_for('default.login_page'))
