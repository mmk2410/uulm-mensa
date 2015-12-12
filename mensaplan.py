#!/bin/env python
"""
Print the Mensaplan of the uni ulm in a fancy cli way
"""

import sys
import urllib.request
import json
import datetime

def get():
    """
    Recieving the JSON file from uulm

    return json data
    """
    url = "http://www.uni-ulm.de/mensaplan/data/mensaplan.json"
    response = urllib.request.urlopen(url)
    data = response.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return data

def print_usage():
    """
    Print the help text
    """
    print("Usage:")
    usage = """
    ./mensaplan.py
    Print the todays menu.

    ./mensaplan.py print [mon, thu, wed, thur, fri]
    Print the menu of the given weekday.
    """
    print(usage)
    print("mmk2410 (c) 2015 MIT License")

if len(sys.argv) >= 2:
    cmd = sys.argv[1]
    if cmd == "help":
        print_usage()
    else:
        if cmd == "mensa":
            place = "Mensa"
        elif cmd == "bistro":
            place = "Bistro"
        elif cmd == "cafeteriab":
            place = "CB"
        elif cmd == "west":
            place = "West"
        elif cmd == "hochschule":
            place = "Prittwitzstr"
        else:
            print("You have to give a place as a agrument")
        plan = get()
        print("Menu:")
        day = datetime.datetime.today().weekday()
        if len(sys.argv) == 3:
            if sys.argv[2] == "mon":
                day = 0
            elif sys.argv[2] == "thu":
                day = 1
            elif sys.argv[2] == "wed":
                day = 2
            elif sys.argv[2] == "thur":
                day = 3
            elif sys.argv[2] == "fri":
                day = 4
            else:
                day = 5
        if day > 4:
            print("There is no information about the menu today.")
            exit(5)
        for meal in plan["weeks"][1]["days"][day][place]["meals"]:
            print(meal["category"] + ": " + meal["meal"])
else:
    print_usage()
