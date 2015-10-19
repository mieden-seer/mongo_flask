from flask import Flask

from modules import math
from modules import math_two

app = Flask(__name__)

app.register_blueprint(math.mod)
app.register_blueprint(math_two.mod_two)