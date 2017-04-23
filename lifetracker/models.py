from peewee import *


class Lights(Model):
    active = IntegerField()
    time_stamp = IntegerField()


class Nest(Model):
    target_temp = IntegerField()
    inside_temp = IntegerField()
    time_stamp = IntegerField()


class Windows(Model):
    open = IntegerField()
    time_stamp = IntegerField()


class Water(Model):
    amount_used = IntegerField()
    time_stamp = IntegerField()


class Electricity(Model):
    amount_used = IntegerField()
    time_stamp = IntegerField()


class Weather(Model):
    temperature = IntegerField()
    precipitating = BooleanField()
    time_stamp = IntegerField()


class Car(Model):
    time_stamp = IntegerField()
    fuel_rate = DoubleField()
    speed = DoubleField()
    odometer = IntegerField()
    target_temp = IntegerField()
    fuel_gauge = IntegerField()


class Bank(Model):
    savings = IntegerField()
    spent = IntegerField()
    time_stamp = IntegerField()


class Fit(Model):
    steps = IntegerField()
    time_stamp = IntegerField()