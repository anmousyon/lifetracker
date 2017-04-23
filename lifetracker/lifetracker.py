''' main lifetracker server '''

import os
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import json
from flask import Flask, render_template, g
from .models import Lights, Nest, Windows, Water, Electricity, Weather, Car, Bank, Fit
from .home import get_home
from .car import get_car
from .life import get_life

lifetracker = Flask(__name__)

# Load default config and override config from an environment variable
lifetracker.config.update(dict(
    DATABASE=os.path.join(lifetracker.root_path, 'lifetracker/lifetracker.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
lifetracker.config.from_envvar('FLASKR_SETTINGS', silent=True)


db = SqliteExtDatabase('lifetracker/lifetracker.db')


def init_db():
    """Initializes the database."""
    db.connect()
    db.create_tables(
        [Lights, Nest, Windows, Water, Electricity, Weather, Car, Bank, Fit],
        safe=True
    )
    get_car()
    get_home()
    get_life()


@lifetracker.cli.command('initdb')
def initdb_command():
    """Creates and fills the database tables."""
    init_db()
    print('Initialized the database.')


@lifetracker.route('/')
def homepage():
    '''homepagepage route'''
    print("/")
    data = {
        {
            "Title": "Energy",
            "Current": 384
        },
        {
            "Title": "Money",
            "Current": 153
        },
        {
            "Title": "Fitness",
            "Current": 356
        }
    }
    json_data = json.dumps(data)
    # return json_data
    return render_template('index.html')


@lifetracker.route('/home')
def home():
    '''home route'''
    print("/home")
    lightdata = Lights.select().order_by(Lights.time_stamp.desc()).get()
    windowdata = Windows.select().order_by(Windows.time_stamp.desc()).get()
    nestdata = Nest.select().order_by(Nest.time_stamp.desc()).get()
    waterdata = Water.select().order_by(Lights.time_stamp.desc()).get()
    elecdata = Electricity.select().order_by(Electricity.time_stamp.desc()).get()
    weatherdata = Weather.select().order_by(Weather.time_stamp.desc()).get()

    data = {
        {
            "Title": "lights",
            "Active": lightdata.active,
            "Target": 0,
            "Rel": "<"
        },
        {
            "Title": "nest",
            "Active": nestdata.inside_temp,
            "Target": nestdata.target_temp,
            "Rel": "="
        },
        {
            "Title": "windows",
            "Active": windowdata.open,
            "Target": 0,
            "Rel": "<"
        },
        {
            "Title": "oustide temp",
            "Active": weatherdata.temperature,
            "Target": "",
            "Rel": ""
        },
        {
            "Title": "outside precip",
            "Active": weatherdata.precipitating,
            "Target": "",
            "Rel": ""
        },
        {
            "Title": "electricity",
            "Active": elecdata.amount_used,
            "Target": 300,
            "Rel": "<"
        },
        {
            "Title": "water",
            "Active": waterdata.amount_used,
            "Target": 300,
            "Rel": "<"
        }
    }
    json_data = json.dumps(data)
    return json_data


@lifetracker.route('/car')
def car():
    '''car route'''
    print("car")
    cardata = Car.select().order_by(Car.time_stamp.desc()).get()
    weatherdata = Weather.select().order_by(Weather.time_stamp.desc()).get()

    # transform cardata into json object
    data = {
        {
            "Title": "fuel_consump",
            "Active": cardata.fuel_consump,
            "Target": 0.5,
            "Rel": "<"
        },
        {
            "Title": "speed",
            "Active": cardata.speed,
            "Target": "",
            "Rel": ""
        },
        {
            "Title": "odometer",
            "Active": cardata.odometer,
            "Target": "",
            "Rel": ""
        },
        {
            "Title": "fuel_gauge",
            "Active": cardata.fuel_gauge,
            "Target": 255,
            "Rel": ">"
        },
        {
            "Title": "ac",
            "Active": cardata.target_temp,
            "Target": 74,
            "Rel": "="
        },
        {
            "Title": "outside temp",
            "Active": weatherdata.temperature,
            "Target": "",
            "Rel": ""
        },
        {
            "Title": "outside precip",
            "Active": weatherdata.precipitating,
            "Target": "",
            "Rel": ""
        }
    }
    json_data = json.dumps(data)
    return json_data


@lifetracker.route('/life')
def life():
    '''life route'''
    print("life")
    bankdata = Bank.select().order_by(Bank.time_stamp.desc()).get()
    fitdata = Fit.select().order_by(Fit.time_stamp.desc()).get()

    # make lifedata json object
    data = {
        {
            "Title": "steps",
            "Active": fitdata.steps,
            "Target": 10000,
            "Rel": ">"
        },
        {
            "Title": "spent",
            "Active": bankdata.spent,
            "Target": 0,
            "Rel": "<"
        },
        {
            "Title": "savings",
            "Active": bankdata.savings,
            "Target": 1000,
            "Rel": ">"
        }
    }
    json_data = json.dumps(data)
    return json_data
