from flask import render_template
from . import home


@home.route('/', methods=['GET'])
def index():
    return render_template('home.html')
