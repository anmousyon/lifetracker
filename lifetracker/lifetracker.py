''' main lifetracker server '''

import os
import sqlite3
from flask import Flask, render_template, g

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'lifetracker.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def main():
    '''main page route'''
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/')
def home():
    '''home route'''
    db = get_db()
    cur = db.execute('select * from nest')
    nestdata = cur.fetchall()
    cur = db.execute('select * from water')
    waterdata = cur.fetchall()
    cur = db.execute('select * from electricity')
    elecdata = cur.fetchall()
    cur = db.execute('select * from weather')
    weatherdata = cur.fetchall()

    return render_template('show_entries.html', homedata=homedata)


@app.route('/')
def car():
    '''care route'''
    db = get_db()
    cur = db.execute('select * from car')
    cardata = cur.fetchall()
    return render_template('show_entries.html', cardata=cardata)


@app.route('/')
def life():
    '''life route'''
    db = get_db()
    cur = db.execute('select * from life')
    lifedata = cur.fetchall()
    return render_template('life.html', lifedata=lifedata)
