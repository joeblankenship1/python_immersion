from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Python & Flask'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Here\s Johnny!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Susie Q!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

