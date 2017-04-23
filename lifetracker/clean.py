import csv


def read_csv(file):
    '''reads telem data from csv into list of lists'''
    data = []
    with open(file) as f:
        datareader = csv.reader(f, delimiter=",")
        for row in datareader:
            data.append(row)
    return data


def delete_row(L):
    for row in L:
        del row[3]
    return L


def writer(file, data):
    with open(file, 'w', newline='') as f:
        csvwriter = csv.writer(f, delimiter=",")
        for row in data:
            csvwriter.writerow(row)


def main():
    data = read_csv('data/car.csv')
    data = delete_row(data)
    writer('data/car2.csv', data)


main()
