# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
import csv
import math
import os
from datetime import datetime
from functools import reduce
from operator import mul
import random
import collections
import numpy as np


class Flights(object):
    legNo = ""
    airport_departure = ""
    date_departure = ""
    hour_departure = ""
    airport_arrival = ""
    date_arrival = ""
    hour_arrival = ""
    pairing_relation = ""
    date_time_arrival = None
    date_time_departure = None
    duration = 0

    # deadhead = False

    def __int__(self):
        self.legNo = self.legNo
        self.airport_departure = self.airport_departure
        self.date_departure = self.date_departure
        self.hour_departure = self.hour_departure
        self.airport_arrival = self.airport_arrival
        self.date_arrival = self.date_arrival
        self.hour_arrival = self.hour_arrival
        self.pairing_relation = self.pairing_relation

    def setDateTime(self):
        self.date_time_departure = datetime.strptime(str(self.date_departure + ' ' + self.hour_departure), "%Y-%m-%d "
                                                                                                           "%H:%M")
        self.date_time_arrival = datetime.strptime(str(self.date_arrival + ' ' + self.hour_arrival), "%Y-%m-%d %H:%M")
        diff = self.date_time_arrival - self.date_time_departure
        seconds_in_hours = diff.seconds / 60 / 60
        days_in_hours = diff.days * 24
        self.duration = seconds_in_hours + days_in_hours

    def __eq__(self, other):
        return self.legNo == other.legNo

    def __hash__(self):
        return hash(('legNo', self.legNo))


class Duties(object):
    legs: list[Flights] = []
    start_date_time = None
    end_date_time = None
    starting_airport = ""
    ending_airport = ""
    total_flying_time = 0
    total_duration = 0

    def __init__(self, legs: list[Flights]):
        self.legs = legs
        self.start_date_time = legs[0].date_time_departure
        self.end_date_time = legs[-1].date_time_arrival
        self.starting_airport = legs[0].airport_departure
        self.ending_airport = legs[-1].airport_arrival
        self.total_flying_time = reduce(mul, [x.duration for x in legs])
        self.total_duration = (self.end_date_time - self.start_date_time).total_seconds() / 60 / 60


class Pairings(object):
    legs: list[Flights] = []
    start_date_time = None
    end_date_time = None
    base_airport = ""
    total_duration = 0
    total_flying_time = 0
    cost = 0

    def __init__(self, duties: list[Duties]):
        self.legs = []
        for duty in duties:
            for leg in duty.legs:
                self.legs.append(leg)
        self.start_date_time = duties[0].start_date_time
        self.end_date_time = duties[-1].end_date_time
        self.base_airport = duties[0].starting_airport
        self.total_flying_time = reduce(mul, [x.total_flying_time for x in duties])
        self.total_duration = (self.end_date_time - self.start_date_time).total_seconds() / 60 / 60

    def __eq__(self, other):
        return self.legs == other.legs


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
