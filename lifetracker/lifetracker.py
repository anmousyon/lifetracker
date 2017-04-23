''' main lifetracker server '''

import os
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import json
from flask import Flask, render_template, g
from .models import Lights, Nest, Windows, Water, Electricity, Weather, Car, Bank, Fit, Sleep, Billdue, BillFuture
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
        [Lights, Nest, Windows, Water, Electricity, Weather, Car, Bank, Fit, Sleep, Billdue, BillFuture],
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
    data = [
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
        },
        {
            "Title": " ",
            "Active": " ",
            "Target": " ",
            "Rel": " "
        }
    ]
    json_data = json.dumps(data)
    return json_data


@lifetracker.route('/home')
def home():
    '''home route'''
    print("/home")
    lightdata = Lights.select().order_by(Lights.time_stamp.desc()).get()
    windowdata = Windows.select().order_by(Windows.time_stamp.desc()).get()
    nestdata = Nest.select().order_by(Nest.time_stamp.desc()).get()
    waterdata = Water.select().order_by(Water.time_stamp.desc()).get()
    elecdata = Electricity.select().order_by(Electricity.time_stamp.desc()).get()
    weatherdata = Weather.select().order_by(Weather.time_stamp.desc()).get()

    data = [
        {
            "Title": "Lights",
            "Active": lightdata.active,
            "Target": 0,
            "Rel": "<"
        },
        {
            "Title": "Nest",
            "Active": nestdata.inside_temp,
            "Target": nestdata.target_temp,
            "Rel": "="
        },
        {
            "Title": "Windows",
            "Active": windowdata.open,
            "Target": 0,
            "Rel": "<"
        },
        {
            "Title": "Temperature",
            "Active": weatherdata.temperature,
            "Target": " ",
            "Rel": " "
        },
        {
            "Title": "Precipitation",
            "Active": weatherdata.precipitating,
            "Target": " ",
            "Rel": " "
        },
        {
            "Title": "Electricity",
            "Active": elecdata.amount_used,
            "Target": 300,
            "Rel": "<"
        },
        {
            "Title": "Water",
            "Active": waterdata.amount_used,
            "Target": 300,
            "Rel": "<"
        },
        {
            "Title": " ",
            "Active": " ",
            "Target": " ",
            "Rel": " "
        }
    ]
    json_data = json.dumps(data)
    return json_data


@lifetracker.route('/car')
def car():
    '''car route'''
    print("car")
    cardata = Car.select().order_by(Car.time_stamp.desc()).get()
    weatherdata = Weather.select().order_by(Weather.time_stamp.desc()).get()

    # transform cardata into json object
    data = [
        {
            "Title": "Fuel Rate",
            "Active": cardata.fuel_rate,
            "Target": 0.5,
            "Rel": "<"
        },
        {
            "Title": "Speed",
            "Active": int(cardata.speed),
            "Target": " ",
            "Rel": " "
        },
        {
            "Title": "Odometer",
            "Active": cardata.odometer,
            "Target": " ",
            "Rel": " "
        },
        {
            "Title": "Fuel Gauge",
            "Active": cardata.fuel_gauge,
            "Target": 255,
            "Rel": ">"
        },
        {
            "Title": "A/C",
            "Active": cardata.target_temp,
            "Target": 74,
            "Rel": "="
        },
        {
            "Title": "Temperature",
            "Active": weatherdata.temperature,
            "Target": " ",
            "Rel": " "
        },
        {
            "Title": "Precipitation",
            "Active": weatherdata.precipitating,
            "Target": " ",
            "Rel": " "
        },
        {
            "Title": " ",
            "Active": " ",
            "Target": " ",
            "Rel": " "
        }
    ]
    json_data = json.dumps(data)
    return json_data


@lifetracker.route('/life')
def life():
    '''life route'''
    print("life")
    bankdata = Bank.select().order_by(Bank.time_stamp.desc()).get()
    fitdata = Fit.select().order_by(Fit.time_stamp.desc()).get()
    sleep = Sleep.select().order_by(Sleep.time_stamp.desc()).get()
    due = Billdue.select().order_by(Billdue.time_stamp.desc()).get()
    future = BillFuture.select().order_by(BillFuture.time_stamp.desc()).get()

    # make lifedata json object
    data = [
        {
            "Title": "Steps",
            "Active": fitdata.steps,
            "Target": 10000,
            "Rel": ">"
        },
        {
            "Title": "Spent",
            "Active": bankdata.spent,
            "Target": 0,
            "Rel": "<"
        },
        {
            "Title": "Savings",
            "Active": bankdata.savings,
            "Target": 1000,
            "Rel": ">"
        },
        {
            "Title": "Sleep",
            "Active": sleep.hours,
            "Target": 8,
            "Rel": ">"
        },
        {
            "Title": "Bills Due",
            "Active": due.amount,
            "Target": 0,
            "Rel": ">"
        },
        {
            "Title": "Future Bills",
            "Active": future.amount,
            "Target": 0,
            "Rel": ">"
        }
    ]
    json_data = json.dumps(data)
    return json_data
