#!/usr/bin/env python3
"""
Print the Mensaplan of the uni ulm in a fancy cli way
"""

import sys
import urllib.request
import json
import datetime

FILES = [
    "http://www.uni-ulm.de/mensaplan/data/mensaplan.json",
    "http://www.uni-ulm.de/mensaplan/data/mensaplan_static.json"
]

def print_usage():
    """Print the help text"""
    print("Usage:")
    usage = """
    ./mensaplan.py place
    Print the todays menu at the place.

    ./mensaplan.py place [mon, tue, wed, thur, fri]
    Print the menu at the place of the given weekday.

    Supported places are:
    Mensa University:    mensa
    Bistro:              bistro
    Burgerbar Southside: burgerbar
    CafeteriaB:          cafeteriab
    Cafeteria West:      west
    West Side Diner:     westside
    Mensa Hochschule:    hochschule
    """
    print(usage)
    print("mmk2410 (c) 2015 MIT License")

def get(url):
    """Recieving the JSON file from uulm"""
    response = urllib.request.urlopen(url)
    data = response.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return data

def get_day():
    """Function for retrieving the wanted day"""
    day = datetime.datetime.today().weekday()
    if len(sys.argv) == 3:
        if sys.argv[2] == "mon":
            day = 0
        elif sys.argv[2] == "tue":
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
    return day

def print_menu(place, static=False):
    """Function for printing the menu

    Keyword arguments:
    place -- name of the cafeteria / mensa
    static -- set true if a static menu exists (default: False)
    """
    day = get_day()
    if static:
        plan = get(FILES[1])
        for meal in plan["weeks"][0]["days"][day][place]["meals"]:
            if place == "Diner":
                print(meal["category"] + " " + meal["meal"])
            else:
                print(meal["category"] + ": " + meal["meal"])
    else:
        plan = get(FILES[0])
        for meal in plan["weeks"][0]["days"][day][place]["meals"]:
            print(meal["category"] + ": " + meal["meal"])

def main():
    """Main function"""
    if len(sys.argv) >= 2:
        cmd = sys.argv[1]
        if cmd == "help":
            print_usage()
        else:
            if cmd == "mensa":
                print_menu("Mensa")
            elif cmd == "bistro":
                print_menu("Bistro")
            elif cmd == "cafeteriab":
                print_menu("CB")
            elif cmd == "west":
                print_menu("West")
            elif cmd == "hochschule":
                print_menu("Prittwitzstr")
            elif cmd == "westside":
                print_menu("Diner", True)
            elif cmd == "burgerbar":
                print_menu("Burgerbar", True)
            else:
                print("[ERROR]: No valid place given")
                print_usage()
    else:
        print("[ERROR]: No argument given")
        print_usage()

main()
