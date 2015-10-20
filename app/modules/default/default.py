from datetime import datetime
from flask import Blueprint
from flask import render_template
from flask import redirect

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
    return redirect('/')