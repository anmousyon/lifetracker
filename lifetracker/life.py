# read in from google fit api or made-up version
# parse it
# put in database

# read transamerica data
# parse it
# put in database

import csv
from .models import Fit, Bank, Sleep, Billdue, BillFuture


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


def insert_due(dataset):
    for data in dataset:
        row = Billdue.create(
            amount=data[0],
            time_stamp=data[1]
        )
        row.save()


def insert_future(dataset):
    for data in dataset:
        row = BillFuture.create(
            amount=data[0],
            time_stamp=data[1]
        )
        row.save()


def insert_sleep(dataset):
    for data in dataset:
        row = Sleep.create(
            status=data[0],
            hours=data[1],
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
    due = read_csv('lifetracker/data/billdue.csv')
    insert_due(due)
    future = read_csv('lifetracker/data/billfuture.csv')
    insert_future(future)
    sleep = read_csv('lifetracker/data/sleep.csv')
    insert_sleep(sleep)
