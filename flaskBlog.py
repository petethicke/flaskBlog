import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

DATABASE = '/tmp/flaskBlog.db'
DEBUG = True
SECRET_KEY = '1987'
USERNAME = 'adminFlaskBlog'
PASSWORD = 'adminFlaskBlog'


app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()