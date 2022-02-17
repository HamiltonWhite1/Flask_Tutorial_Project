from flask import render_template
from app import app_inst

@app_inst.route('/')
@app_inst.route('/index')
def index():
    user = {
        'username': 'Hamilton',
        'dog': 'Zion',
        'wife': 'Jenna'
        
        }

    return render_template('index.html', title='Home', user=user)