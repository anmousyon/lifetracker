import csv
import random


def writer(file, data):
    with open(file, 'w') as f:
        csvwriter = csv.writer(f, delimiter=",")
        for row in data:
            csvwriter.writerow(row)


def gen_data(data):
    ts = 1492882310
    future = 875
    for x in range(1000):
        rand = random.randint(0, 250)
        if rand == 2:
            future -= 125
        data.append([future, ts-x])
    return data


def main():
    data = []
    data = gen_data(data)
    writer('data/billfuture.csv', data)


main()
