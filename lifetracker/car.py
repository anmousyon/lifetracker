import csv
from .models import Car


def read_csv(file):
    '''reads telem data from csv into list of lists'''
    data = []
    with open(file) as f:
        datareader = csv.reader(f, delimiter=",")
        for row in datareader:
            data.append(row)
    return data


def insert(dataset):
    ''' insert data into database '''
    for data in dataset:
        row = Car.create(
            time_stamp=data[0],
            fuel_rate=data[1],
            speed=data[2],
            odometer=data[3],
            target_temp=data[4],
            fuel_gauge=data[5]
        )
        row.save()


def get_car():
    data = read_csv('lifetracker/data/car2.csv')
    insert(data)
