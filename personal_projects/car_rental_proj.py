import names
import random
from random_address import real_random_address
import os
import datetime

COLOR_RESET = '\x1b[0m'
COLOR_BLUE = '\x1b[0;34;48m'
COLOR_BLUE_BG = '\x1b[7;34;48m'
COLOR_PURPLE = '\x1b[0;35;48m'
COLOR_RED = '\x1b[0;31;48m'
COLOR_RED_BG = '\x1b[7;31;48m'
COLOR_TEAL_BG = '\x1b[7;36;48m'
COLOR_GREEN = '\x1b[7;36;48m'
COLOR_YELLOW = '\x1b[7;33;48m'
OKCYAN = '\033[96m'
FAIL = '\033[91m'
WARNING = '\033[93m'
OKGREEN = '\033[92m'


def PrintTable():
  print('╒══════════╤═══════════════╤══════════════╤════════════════╕')
  print('│   Car ID │ Company       │ Model        │ Cost Per Day   │')
  print('╞══════════╪═══════════════╪══════════════╪════════════════╡')
  print('│      782 │ Chervolet     │ Spark        │ $11            │')
  print('├──────────┼───────────────┼──────────────┼────────────────┤')
  print('│      783 │ Volkswagen    │ Passat       │ $55            │')
  print('├──────────┼───────────────┼──────────────┼────────────────┤')
  print('│      784 │ Audi          │ A5 Sportback │ $66            │')
  print('├──────────┼───────────────┼──────────────┼────────────────┤')
  print('│      785 │ Mercedes Benz │ Gle          │ $139           │')
  print('╘══════════╧═══════════════╧══════════════╧════════════════╛')
  print('')


def Ascii():
  print(OKCYAN +
        '_________                __________               __         .__   ' +
        COLOR_RESET)
  print(OKCYAN +
        '\_   ___ \_____ _______  \______   \ ____   _____/  |______  |  |  ' +
        COLOR_RESET)
  print(OKCYAN +
        '/    \  \/\__  \\_  __ \  |       _// __ \ /    \   __\__  \ |  |  ' +
        COLOR_RESET)
  print(OKCYAN +
        '\     \____/ __ \|  | \/  |    |   \  ___/|   |  \  |  / __ \|  |__' +
        COLOR_RESET)
  print(
    OKCYAN +
    ' \______  (____  /__|     |____|_  /\___  >___|  /__| (____  /____/ ' +
    COLOR_RESET)
  print(OKCYAN +
        '        \/     \/                \/     \/     \/          \/      ' +
        COLOR_RESET)


def Greeting():
  print('')
  print(
    WARNING +
    f"Hello, welcome to Rithik's Car Rental. My name is {names.get_full_name()} and this company has been running for a pretty long time."
    + COLOR_RESET)
  print('')
  print(
    OKGREEN +
    "Here are the available list of cars, enter the car's ID number to rent:" +
    COLOR_RESET)
  print('')


def RentalAsk():
  rental_ask_result = input(WARNING + 'Would you like to rent? (' +
                            COLOR_RESET + OKGREEN + 'y' + COLOR_RESET + '/' +
                            COLOR_RED + 'n' + COLOR_RESET + WARNING + '): ' +
                            COLOR_RESET)

  if rental_ask_result == 'y':
    print('')
    print(COLOR_PURPLE + "Let's begin!" + COLOR_RESET)
  elif rental_ask_result == 'n':
    print('')
    print(COLOR_PURPLE + 'Thanks for Visiting!' + COLOR_RESET)
    print('')
    exit()
    os.system("clear")
  else:
    print('')
    print(COLOR_RED + 'Enter a valid option' + COLOR_RESET)
    print('')
    RentalAsk()

    print('')


def CarSelection():
  global cost
  global selected_car
  selected_car = ''
  cost = ''
  print('')
  car_selection_result = input(OKCYAN + 'Please enter a Car ID: ' +
                               COLOR_RESET)
  if car_selection_result == "782":
    print('')
    cost = int(11)
    print(OKGREEN + 'Chervolet Spark Selected. The Cost is $11 per day.' +
          COLOR_RESET)
    selected_car = 'Chervolet Spark'
  elif car_selection_result == "783":
    print('')
    cost = int(55)
    print(OKGREEN + 'Volkswagen Passat Selected. The Cost is $55 per day.' +
          COLOR_RESET)
    selected_car = 'Volkswagen Passat'
  elif car_selection_result == "784":
    print('')
    cost = int(66)
    print(OKGREEN + 'Audi A5 Sportback Selected. The Cost is $66 per day.' +
          COLOR_RESET)
    selected_car = 'Audi A5 Sportback'
  elif car_selection_result == "785":
    print('')
    cost = int(139)
    print(OKGREEN + 'Mercedes Benz Gle Selected. The Cost is $139 per day.' +
          COLOR_RESET)
    selected_car = 'Mercedes Benz Gle'
  else:
    print('')
    print(COLOR_RED + 'Please enter a valid Car ID' + COLOR_RESET)
    CarSelection()


def Quantity():
  global total
  print('')
  try:
    quantity_result = input(
      OKCYAN +
      'How many cars would you like? (Please enter a number: 1,2,3...etc): ' +
      COLOR_RESET)
    print('')
    quantity_result_int = int(quantity_result)
    total = int(cost) * quantity_result_int
    print(COLOR_PURPLE + f'The cost of your rental is ${total}' + COLOR_RESET)
    print('')
  except ValueError:
    print(COLOR_RED + 'Enter a valid amount' + COLOR_RESET)
    print('')
    Quantity()


def CountDays():
  global finaltotal
  try:
    count_days_result = input(OKCYAN +
                              "How many days would you like this car for?: " +
                              COLOR_RESET)
    finaltotal = int(count_days_result) * int(total)
    print('')
    print(COLOR_PURPLE + f'The total cost of your rental is ${finaltotal}' +
          COLOR_RESET)
    print('')
  except ValueError:
    print('')
    print(COLOR_RED + 'Enter a valid amount' + COLOR_RESET)
    print('')
    CountDays()


def ValidateDates(date_text):
  try:
    datetime.datetime.strptime(date_text, '%m-%d-%Y')
  except ValueError:
    print('')
    print(COLOR_RED + 'Enter a valid date (MM-DD-YYYY)' + COLOR_RESET)
    print('')


def SelectDates():
  global pickup_date
  global dropoff_date
  pickup_date = input(OKCYAN + 'Please enter your pickup date (MM-DD-YYYY): ' +
                      COLOR_RESET)
  ValidateDates(pickup_date)
  print('')
  dropoff_date = input(OKCYAN +
                       'Please enter your dropoff date (MM-DD-YYYY): ' +
                       COLOR_RESET)
  print('')
  ValidateDates(dropoff_date)


def Timing():
  global pickup_time
  global dropoff_time
  print('')
  pickup_time = input(
    COLOR_PURPLE +
    f"What time would you like your {selected_car} to arrive?: " + COLOR_RESET)
  print('')
  dropoff_time = input(
    COLOR_PURPLE +
    f"What time would you like your {selected_car} to drop you off?: " +
    COLOR_RESET)
  print('')


def Payment():
  name_result = input(OKCYAN + "What's your name?: " + COLOR_RESET)
  random_num = str(random.randint(1, 1000000))
  print('')
  verification_result = input(
    COLOR_PURPLE +
    f'{name_result}, please type in {random_num} to verify that you are a human: '
    + COLOR_RESET)
  if random_num == verification_result:
    print('')
    am_or_pm = ['AM', 'PM']
    print('')
    print(OKGREEN +
          f"Payment of ${finaltotal} Success! Thanks for renting a car." +
          COLOR_RESET)
    print('')
    print(
      OKGREEN +
      f"Your {selected_car} will pick you up at {real_random_address()['address1']}, {real_random_address()['city']}, {real_random_address()['state']} {real_random_address()['postalCode']}. It will arrive at your house at {pickup_time} on {pickup_date} and drop you off at {dropoff_time} on {dropoff_date}"
      + COLOR_RESET)
    print('')
  else:
    print('')
    print(COLOR_RED + 'Please try again' + COLOR_RESET)
    print('')
    Payment()


def PaymentProceed():
  payment_ask_result = input(WARNING + 'Would you like to pay? (' +
                             COLOR_RESET + OKGREEN + 'y' + COLOR_RESET + '/' +
                             COLOR_RED + 'n' + COLOR_RESET + WARNING + '): ' +
                             COLOR_RESET)

  if payment_ask_result == 'y':
    print('')
    Payment()
  elif payment_ask_result == 'n':
    print('')
    print(COLOR_PURPLE + 'Thanks for Visiting!' + COLOR_RESET)
    print('')
    exit()
    os.system("clear")

  else:
    print('')
    print(COLOR_RED + 'Enter a valid option' + COLOR_RESET)
    print('')
    RentalAsk()

  print('')


def CarRental():
  Ascii()
  Greeting()
  PrintTable()
  RentalAsk()
  CarSelection()
  Quantity()
  CountDays()
  SelectDates()
  Timing()
  PaymentProceed()


while True:
  CarRental()
  input(COLOR_BLUE + 'Type any key to continue: ' + COLOR_RESET)
  os.system("clear")
