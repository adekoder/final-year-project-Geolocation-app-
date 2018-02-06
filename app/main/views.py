from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/search')
def search():
    return render_template('main/search.html')

@main.route('/explore')
def explore():
    return render_template('main/explore.html')


@main.route('/map')
def show_map():
    return render_template('main/maps.html')
 