# read in nest data
# parse it
# put in database

# read in water/electricity meters
# parse it
# put in database

# access weather api
# parse data
# put in database

import csv
from .models import Lights, Windows, Nest, Water, Electricity, Weather


def read_csv(file):
    '''reads data from csv into list of lists'''
    data = []
    with open(file) as f:
        datareader = csv.reader(f, delimiter=",")
        for row in datareader:
            data.append(row)
    return data


def insert_lights(dataset):
    for data in dataset:
        row = Lights.create(
            active=data[0],
            time_stamp=data[1]
        )
        row.save()


def insert_windows(dataset):
    for data in dataset:
        row = Windows.create(
            open=data[0],
            time_stamp=data[1]
        )
        row.save()


def insert_nest(dataset):
    for data in dataset:
        row = Nest.create(
            target_temp=data[0],
            inside_temp=data[1],
            time_stamp=data[2]
        )
        row.save()


def insert_water(dataset):
    for data in dataset:
        row = Water.create(
            amount_used=data[0],
            time_stamp=data[1]
        )
        row.save()


def insert_elec(dataset):
    for data in dataset:
        row = Electricity.create(
            amount_used=data[0],
            time_stamp=data[1]
        )
        row.save()


def insert_weather(dataset):
    for data in dataset:
        row = Weather.create(
            temperature=data[0],
            precipitating=data[1],
            time_stamp=data[2]
        )
        row.save()


def get_home():
    '''get all life data'''
    lights = read_csv('lifetracker/data/lights.csv')
    insert_lights(lights)
    windows = read_csv('lifetracker/data/windows.csv')
    insert_windows(windows)
    nest = read_csv('lifetracker/data/nest.csv')
    insert_nest(nest)
    water = read_csv('lifetracker/data/water.csv')
    insert_water(water)
    elec = read_csv('lifetracker/data/elec.csv')
    insert_elec(elec)
    weather = read_csv('lifetracker/data/weather.csv')
    insert_weather(weather)
