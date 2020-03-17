#  all  the imports
import argparse
import colored
import requests
from colored import stylize



parser  = argparse.ArgumentParser()
parser.add_argument("Hydrogen", help=stylize("An open-source python Library for checking the avalibily of a website, created by vatsalay khobragade.", colored.fg("royal_blue_1")) )


parser.add_argument("web", type=str, help=stylize("Name of the website you want to check the avalibility", colored.fg("royal_blue_1")))

parser.add_argument("--version", help=stylize("Version 0.0.1", colored.fg("royal_blue_1")), action="store_true")




args = parser.parse_args()

if args.version:
    print("Version 0.0.1")
else:
    pass


if args.web:
    status = requests.get(args.web)
    final = (status.status_code)
    if final == 200:
        print(stylize("The site is Live", colored.fg("royal_blue_1")))
    elif final == 404:
        print("The site is Dead")
else:
    print("we need arguments")
# print(args.Hydrogen)
