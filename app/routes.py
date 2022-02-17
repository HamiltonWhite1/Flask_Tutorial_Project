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
    posts = [
        {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Boston'
    }, {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie is so weird!'
    }, {
        'author': {'username': 'Deryl'},
        'body': 'I just had the best chorizo!'
    } ]
    return render_template('index.html', tile='Home', user=user, posts=posts)