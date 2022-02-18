from flask import render_template, flash, redirect
from app import app_inst
from app.forms import LoginForm

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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app_inst.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign in', form=form)