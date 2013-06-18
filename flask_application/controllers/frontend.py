#!/usr/bin/env python

import datetime

from flask import Blueprint, render_template, request
from flask_application import app

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template('index.html', config=app.config,)
            
@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")
    
@frontend.route("/contact")
def contact():
    return render_template('contact.html',
                config=app.config,
                now=lambda: "Contact TODO")