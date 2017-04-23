import csv
import random


def writer(file, data):
    with open(file, 'w') as f:
        csvwriter = csv.writer(f, delimiter=",")
        for row in data:
            csvwriter.writerow(row)


def gen_data(data):
    ts = 1492882310
    rain = False
    temp = 74
    for x in range(1000):
        rand = random.randint(0, 9)
        if rand == 0:
            rain = not rain
        if rand == 1:
            temp = 75
        if rand == 2:
            temp == 75
        if rain:
            data.append([temp, "rain", ts-x])
        else:
            data.append([temp, "clear", ts-x])
    return data


def main():
    data = []
    data = gen_data(data)
    writer('data/weather.csv', data)


main()
