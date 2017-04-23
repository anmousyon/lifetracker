# read in from google fit api or made-up version
# parse it
# put in database

# read transamerica data
# parse it
# put in database

import csv
from .models import Fit, Bank


def read_csv(file):
    '''reads data from csv into list of lists'''
    data = []
    with open(file) as f:
        datareader = csv.reader(f, delimiter=",")
        for row in datareader:
            data.append(row)
    return data


def insert_fit(dataset):
    for data in dataset:
        row = Fit.create(
            steps=data[0],
            time_stamp=data[1]
        )
        row.save()


def insert_bank(dataset):
    for data in dataset:
        row = Bank.create(
            savings=data[0],
            spent=data[1],
            time_stamp=data[2]
        )
        row.save()


def get_life():
    '''get all life data'''
    fit = read_csv('lifetracker/data/fit.csv')
    insert_fit(fit)
    bank = read_csv('lifetracker/data/bank.csv')
    insert_bank(bank)
