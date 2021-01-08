"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from fapl import app


@app.route('/')
@app.route('/index')
def index():
    """Renders the home page."""
    return render_template(
        'base.html',
        title='Home Page',
        year=datetime.now().year,
    )

app.add_url_rule('/', 'index', index)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,  {}!</h1>'.format(name)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.jade',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
    
@app.route('/viewlog')
def view_the_log()-> 'html':
    #with open('vsearch.log') as log:
    #    contents = log.read()
    #return escape(contents)
    contents=[]
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form data', 'Remote addr', 'User agent', 'Results')
    #return str(contents)
    return render_template('viewlog.html', 
                                the_title='View Log',
                                the_row_titles = titles,
                                the_data = contents,)