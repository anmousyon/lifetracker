# read in telemmetry data
# parse it
# put in database with timestamps

import csv


def read_telem(file):
    '''reads telem data from csv into list of lists'''
    telemdata = []
    with open(file) as f:
        telemdata = csv.reader(f, delimiter=",")
    return telemdata


def combine(data):
    '''combines telem data by timestamp'''
    # split data into list of lists of lists by timestamp
    combined = []
    ts_to_data = {}
    for ts in data:
        # create a group of similar timestamps
        ts_to_data[ts[0]].append(ts)
    for _, v in ts_to_data:
        combined.append(v)

def smooth(data):
    '''smooth out the data '''
    for ts in data:
        # combine lists by getting median of each continous data point
        # take newest value for any booleans


def insert(data, db):
    ''' insert data into database '''
    for ts in data:
        # insert data into database


def get_cardata(db):
    data = read_telem('telem.csv')
    data = combine(data)
    data = smooth(data)
    insert(data, db)