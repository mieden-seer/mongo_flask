from flask import Flask
from flask import g

from modules.math import math
from modules import math_two
from modules import default
from modules import posts
from modules import users

from pymongo import MongoClient

app = Flask(__name__)

def get_main_collection():
    client = MongoClient('mongodb://localhost:27017/')
    collect = client.usersdb.users
    return collect

@app.before_request
def before_request():
    postConn = get_main_collection()
    g.usersdb = users.UsersDB(conn=postConn)

@app.teardown_request
def teardown_request(exception):
    postdb = getattr(g, 'postdb', None)
    if postdb is not None:
        postdb.close()

app.register_blueprint(math.mod, url_prefix="/math")
app.register_blueprint(math_two.mod_two)
app.register_blueprint(default.mod)
app.register_blueprint(posts.mod, url_prefix="/posts")
app.register_blueprint(users.ur)