
from time import sleep
def main():
    print("")
    print("Temperature Converter")
    print("This program converts Fahrenheit to Celsius and Celsius to Fahrenheit")
    z = input("What would you like to convert to: ")
    if z == "c" or z == "Celsius":
        x = eval(input("How many Fahrenheit would you like to convert to Celsius: "))
        Celsius = (5 / 9) * (x - 32)
        print(Celsius)
    elif z == "f" or z ==  "Fahrenheit":
        y = eval(input("How many Celsius would you like to convert to Fahrenheit: "))
        Fahrenheit = (9 / 5) * y + 32
        print(Fahrenheit)
    else:
        print("You need to choose")
        sleep(1)
        main()
main()