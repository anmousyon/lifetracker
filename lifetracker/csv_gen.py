import csv
import random


def writer(file, data):
    with open(file, 'w', newline='') as f:
        csvwriter = csv.writer(f, delimiter=",")
        for row in data:
            csvwriter.writerow(row)


def gen_data(data):
    ts = 1492882310
    savings = 1234
    spent = 731
    for x in range(1000):
        rand = random.randint(0, 9)
        if rand == 0:
            spent -= 4
            savings += 4
        elif rand == 1:
            spent -= 3
            savings += 3
        data.append([savings, spent, ts-x])
    return data


def main():
    data = []
    data = gen_data(data)
    writer('bank.csv', data)


main()
