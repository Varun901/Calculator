from time import sleep


class Purse (object):

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.money = 0.0
        self.misc_items = []

    def add_money(self):
        amount = float(input("Enter how much money you want to add: "))
        self.money += amount
        return self.money

    def remove_money(self):
        amount = float(input("Enter how much money you want to remove: "))
        self.money -= amount
        return self.money

    def get_name(self):
        return self.name

    def add_items(self):
        num_items = int(input('Enter how many items you want to add: '))
        for i in range(num_items):
            print("Item #",(i+1))
            item = input("Enter the first item you would like to add: ")
            self.misc_items.append(item)
        return self.misc_items

    def remove_items(self):
        print(self.misc_items)
        for i in range(len(self.misc_items)):
            print(self.misc_items[i], "=", i)
        num_items = int(input("How many items would you like to remove: "))
        for i in range(num_items):
            print("Item #", (i + 1))
            item = int(input("Enter the first item number you would like to remove: "))
            self.misc_items.remove(self.misc_items[item])
        return self.misc_items

    def contents(self):
        print(self.name)
        print(self.colour)
        print(self.money)
        print(self.misc_items)
def main():
    name = input("What's your name? ")
    colour = input("What the colour of your purse? ")
    purse1 = Purse(name, colour)
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