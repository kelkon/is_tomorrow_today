# get current time and sun rise time (can be found using current time)
# and returns yes if the time is between mid night and the sun rise time
# if sun rise time cannot be found, default to 8am
# otherwise return no

import datetime
from astral.sun import sun
from astral import LocationInfo
from astral.geocoder import database, lookup
import sys

default_sunrise_time = 8

def is_today_tomorrow():
    try:
        city = lookup("Sydney", database())
        s = sun(city.observer, date=datetime.date.today(), tzinfo=city.timezone)
        sunrise_time = (s['sunrise'].hour, s['sunrise'].minute)
    except:
        sunrise_time = (8,0)

    tmp = datetime.datetime.now()
    current_time = (tmp.hour, tmp.minute)
    del tmp

    if sunrise_time[0] > current_time[0]:
        return 'yes'
    if sunrise_time[0] < current_time[0]: 
        return 'no'
    if sunrise_time[0] == current_time[0]:
        if sunrise_time[1] > current_time[1]:
            return 'yes'
        else:
            return 'no'

print(is_today_tomorrow())



