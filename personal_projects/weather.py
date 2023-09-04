import requests, json
import sys
import os
from time import sleep

COLOR_RESET = '\x1b[0m'
COLOR_BLUE = '\x1b[0;34;48m'
COLOR_BLUE_BG = '\x1b[7;34;48m'
COLOR_PURPLE = '\x1b[0;35;48m'
COLOR_RED = '\x1b[0;31;48m'
COLOR_RED_BG = '\x1b[7;31;48m'
COLOR_TEAL_BG = '\x1b[7;36;48m'
COLOR_GREEN = '\x1b[7;36;48m'
COLOR_YELLOW = '\x1b[7;33;48m'

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

global city_name

# API Key - Remains Private
api_key = "28329d118558160b46dbf4e49bae7e58"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def Intro():
    print('')
    for char in COLOR_BLUE + BOLD + "Welcome to the Weather App. Created by Rithik Samanthula." + COLOR_RESET:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')


def Proceed():
    print('')

    for char in OKCYAN + BOLD + "Would you like to proceed? " + COLOR_RESET + BOLD + "(" + COLOR_RESET + OKGREEN + BOLD + "y" + COLOR_RESET + BOLD + "/" + COLOR_RESET + FAIL + BOLD + "n" + COLOR_RESET + BOLD + "): " + COLOR_RESET:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

    proceed_result = input(WARNING + BOLD + ">> " + COLOR_RESET)

    if proceed_result == "y":
        print('')
        for char in OKGREEN + BOLD + "Alright, lets proceed with checking the weather in your city" + COLOR_RESET:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
        print('')

        ApiFetch()
    elif proceed_result == "n":
        print('')
        for char in COLOR_RED + BOLD + "Thanks for checking the app out" + COLOR_RESET:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
            os.system("clear")
    else:
        print('')
        for char in COLOR_RED + BOLD + "Please type in a valid option" + COLOR_RESET:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
        print('')
        Proceed()


def ApiFetch():
    print('')
    for char in OKCYAN + BOLD + "Enter your city name: " + COLOR_RESET:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

    city_name = input(WARNING + BOLD + ">> " + COLOR_RESET)

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values

        print('')

        for char in COLOR_BLUE + BOLD + "\nTemperature (Kelvin): " + COLOR_RESET + str(current_temperature):
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

        for char in COLOR_BLUE + BOLD + "\nAtmospheric Pressure (hPa): " + COLOR_RESET + str(current_pressure):
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

        for char in COLOR_BLUE + BOLD + "\nHumidity (%): " + COLOR_RESET + str(current_humidity):
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

        for char in COLOR_BLUE + BOLD + "\nWeather Description: " + COLOR_RESET + str(weather_description):
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

        print('')

    else:

        print('')
        for char in COLOR_RED + BOLD + "City not found. Try entering a different or a valid city" + COLOR_RESET:
            sleep(0.002)
            sys.stdout.write(char)
            sys.stdout.flush()

        ApiFetch()


def Start():
    Intro()
    Proceed()


Start()

input(COLOR_BLUE + BOLD + 'Type any key to continue: ' + COLOR_RESET)
os.system("clear")