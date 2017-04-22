# read in nest data
# parse it
# put in database

# read in water/electricity meters
# parse it
# put in database

# access weather api
# parse data
# put in database


def read_csv(file):
    '''reads data from csv into list of lists'''
    data = []
    with open(file) as f:
        data = csv.reader(f, delimiter=",")
    return data


def insert_nest(db, data):
    db.execute(
        'insert into entries (title, text) values (?, ?)',
        [
            request.form['title'],
            request.form['text']
        ]
    )


def insert_water(db, data):
    # insert data into database


def insert_elec(db, data):
    # insert data into database


def insert_weather(db, data):
    # insert data into database


def get_home(db):
    '''get all life data'''
    nest = read_csv('nest.csv')
    insert_nest(db, nest)
    water = read_csv('water.csv')
    insert_water(db, water)
    elec = read_csv('elec.csv')
    insert_elec(db, elec)
    weather = read_csv('weather.csv')
    insert_weather(db, weather)
