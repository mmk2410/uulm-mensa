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
    ./mensaplan.py print
    Um das heutige Menue auszugeben.

    ./mensaplan.py print [mon, thu, wed, thur, fri]
    Um das Menue des jeweiligen Tasges auszugeben.
    """
    print(usage)
    print("mmk2410 (c) 2015 MIT License")

if len(sys.argv) >= 2:
    cmd = sys.argv[1]
    if cmd == "print":
        plan = get()
        print("Mensplan:")
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
            print("Heute gibt es nichts zu essen. Bloed gelaufen :(")
            exit(5)
        for meal in plan["weeks"][1]["days"][day]["Mensa"]["meals"]:
            print(meal["category"] + ": " + meal["meal"])
    else:
        print_usage()
else:
    print_usage()
