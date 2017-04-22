# read in from google fit api or made-up version
# parse it
# put in database

# read transamerica data
# parse it
# put in database


def read_csv(file):
    '''reads data from csv into list of lists'''
    data = []
    with open(file) as f:
        data = csv.reader(f, delimiter=",")
    return data


def insert_fit(db, data):
    # insert data into database


def insert_bank(db, data):
    # insert data into database

def get_life(db):
    '''get all life data'''
    fit = read_csv('fit.csv')
    insert_fit(db, fit)
    bank = read_csv('bank.csv')
    insert_bank(db, bank)
