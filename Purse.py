from time import sleep


class Purse (object):

    def __init__(self, name, colour, money):
        self.name = name
        self.colour = colour
        self.money = money
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
