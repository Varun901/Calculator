# File: Temperature_Converter.py
# This program allows for temperature conversion between Celsius, Fahrenheit and Kelvin
# In this program the user is able to choose the conversion they need and how much to convert
# In order to add a slight delay in the program response a sleep function was added
from time import sleep
from datetime import datetime
now = datetime.now()


def main():
    print("")
    print("The calculator is starting up...")
    print('%02d/%02d/%04d  %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
    sleep(1)
    print("")
    print("Temperature Converter")
    print("This program converts Temperature, specifically Celsius, Fahrenheit and Kelvin!")
    convert_from = input("What would you like to convert: ")
    if convert_from == "c" or convert_from == "Celsius":
        convert_to = input("What would you like to convert Celsius to: ")
        if convert_to == "f" or convert_to == "Fahrenheit":
            y = float(input("How many Celsius would you like to convert to Fahrenheit: "))
            fahrenheit = (9 / 5) * y + 32
            print('The temperature is', fahrenheit, "degrees Fahrenheit.")
        elif convert_to == "k" or convert_to == "Kelvin":
            x = float(input("How many Celsius would you like to convert to Kelvin: "))
            kelvin = x + 273.15
            print('The temperature is', kelvin, "Kelvin.")
        else:
            print("You need to choose Fahrenheit or Kelvin!")
            sleep(1)
            main()
    elif convert_from == "f" or convert_from == "Fahrenheit":
        convert_to = input("What would you like to convert Fahrenheit to: ")
        if convert_to == "k" or convert_to == "Kelvin":
            y = float(input("How many Fahrenheit would you like to convert to Kelvin: "))
            kelvin = (y + 459.67) * (5/9)
            print('The temperature is', kelvin, "Kelvin.")
        elif convert_to == "c" or convert_to == "Celsius":
            x = float(input("How many Fahrenheit would you like to convert to Celsius: "))
            celsius = (5 / 9) * (x - 32)
            print('The temperature is', celsius, "degrees Celsius.")
        else:
            print("You need to choose Celsius or Kelvin!")
            sleep(1)
            main()
    elif convert_from == "k" or convert_from == "Kelvin":
        convert_to = input("What would you like to convert Kelvin to: ")
        if convert_to == "c" or convert_to == "Celsius":
            y = float(input("How many Kelvin would you like to convert to Celsius: "))
            celsius = y - 273.15
            print('The temperature is', celsius, "degrees Celsius.")
        elif convert_to == "f" or convert_to == "Fahrenheit":
            x = float(input("How many Kelvin would you like to convert to Fahrenheit: "))
            fahrenheit = (9/5) * x - 459.67
            print('The temperature is', fahrenheit, "degrees Fahrenheit.")
        else:
            print("You need to choose Celsius or Fahrenheit!")
            sleep(1)
            main()
    else:
        print("You need to choose")
        sleep(1)
        main()
main()