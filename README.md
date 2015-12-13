#Mensplan

A python script for viewing the menu of the canteens of the Studierendenwerk Ulm in Ulm. The supported canteens are:

 - Mensa University
 - CafeteriaB
 - Southside Burgerbar
 - Bistro
 - Cafeteria West
 - WestSideDiner
 - Mensa Hochschule

##Usage
After making the mensaplan.py executable with `chmod +x mensaplan.py` you have the following options:
```
./mensaplan.py place
Print the todays menu at the place.

./mensaplan.py place [mon, thu, wed, thur, fri]
Print the menu at the place of the given weekday.

Supported places are:
Mensa University:    mensa
Bistro:              bistro
Burgerbar Southside: burgerbar
CafeteriaB:          cafeteriab
Cafeteria West:      west
West Side Diner:     westside
Mensa Hochschule:    hochschule
```

## Credits
Thanks a lot at (https://github.com/seder)[Thomas Lukaseder] and his (https://github.com/seder/mensaplan-parser)[Mensaplan Parser] as well as the Studierendenwerk Ulm for providing the data.

## License

MIT License
