#Mensaplan
[![GitHub
release](https://img.shields.io/github/release/qubyte/rubidium.svg)]()
[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)]()
[![Twitter Follow](https://img.shields.io/twitter/follow/shields_io.svg?style=social)]()

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
Thanks a lot at [Thomas Lukaseder](https://github.com/seder) and his [Mensaplan Parser](https://github.com/seder/mensaplan-parser).

## License

MIT License
