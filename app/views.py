"""
  Routing for your application
"""

from . import *
from flask import render_template, request, redirect, url_for, jsonify, make_response, session, flash, g
from functools import wraps, update_wrapper
import time
from datetime import datetime


"""
  Standard Dependencies
"""
css_list = [
]

js_list = [
]

component_list = [
'/static/bower_components/todo-element/todo-element.html',
'/static/bower_components/todo-app/todo-app.html',
'/static/bower_components/page-shell/page-shell.html'
]

@app.route('/')
def home():
  return render_template('home.html', cssdep=css_list, jsdep=js_list, componentdep=component_list)

@app.route('/login')
def login():
  return render_template('login.html', cssdep=css_list, jsdep=js_list, componentdep=component_list)

@app.route('/time')
def getTime():
  data = {'time': int(time.time())}
  resp = make_response()
  resp = jsonify(data)
  return resp

if __name__ == '__main__':
  app.run(debug=True)