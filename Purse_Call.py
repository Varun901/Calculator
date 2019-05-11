from Purse import Purse
from time import sleep

def main():
    name = input("What's your name? ")
    colour = input("What the colour of your purse? ")
    money = int(input("How much money do you have in your purse right now? "))
    purse1 = Purse(name, colour, money)
    while True:
        print("Hi", purse1.get_name())
        print("What would you like to do with your purse? ")
        print("1. Add Money", "2. Remove Money", "3. Add Items", "4. Remove items", "5. Leave", sep = "\n")
        choice = int(input("Enter choice here: "))
        if choice == 1:
            purse1.add_money()
            sleep(1)
            purse1.contents()
            sleep(1)
        elif choice == 2:
            purse1.remove_money()
            sleep(1)
            purse1.contents()
            sleep(1)
        elif choice == 3:
            purse1.add_items()
            sleep(1)
            purse1.contents()
            sleep(1)
        elif choice == 4:
            purse1.remove_items()
            sleep(1)
            purse1.contents()
            sleep(1)
        elif choice == 5:
            print("Goodbye")
            break
        else:
            print("Invalid Option, Try Again")
            sleep(1)
            purse1.contents()
            sleep(1)


main()