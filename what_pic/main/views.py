from flask import render_template, session, url_for, current_app, redirect
from . import main
from .forms import ImageUrlForm

@main.route('/')
def index():
    return render_template('index.html')
