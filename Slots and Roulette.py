from time import sleep
from random import randint

def slots (money, num_times):
    required_funds = num_times*4
    if money >= required_funds:
        money = money - required_funds
        print("Thank you for playing the Slots!")
        sleep(1)
        for i in range(num_times):
            win = randint(1, 4)
            choice = int(input("Enter a number between 1 and 4: "))
            if choice == win:
                print("Ayyyyy my g! Congrats you won!!!!")
                print()
                sleep(0.5)
                money = money + 8
            elif choice != win and choice >= 1 and choice <= 4:
                print("Shocking, you didn't win anything")
                print()
                sleep(0.5)
            else:
                print("That number is not between 1 and 4")
                valid_choice = int(input("Enter a valid number between 1 and 4: "))
                if valid_choice == win:
                    print("Ayyyyy my g! Congrats you won!!!!")
                    print()
                    sleep(0.5)
                    money = money + 8
                elif valid_choice != win and valid_choice >= 1 and valid_choice <= 4:
                    print("Shocking, you didn't win anything")
                    print()
                    sleep(0.5)
                else:
                    print("That number is not between 1 and 4", "That was your last chance", "You lose", sep="\n")
                    print()
                    sleep(0.5)
    else:
        print("Sorry, insufficient funds.")
        print()
        sleep(0.5)
    return money

def roulette (money, num_times):
    required_funds = num_times*10
    if money >= required_funds:
        money = money - required_funds
        print("Thank you for playing Roulette!")
        sleep(1)
        for i in range(num_times):
            win = randint(1, 39)
            choice = int(input("Enter a number between 1 and 39: "))
            if choice == win:
                print("Ayyyyy my g! Congrats you won!!!!")
                print()
                sleep(0.5)
                money = money + 360
            elif choice != win and choice >= 1 and choice <= 39:
                print("Shocking, you didn't win anything")
                print()
                sleep(0.5)
            else:
                print("That number is not between 1 and 39")
                valid_choice = int(input("Enter a valid number between 1 and 39: "))
                if valid_choice == win:
                    print("Ayyyyy my g! Congrats you won!!!!")
                    print()
                    sleep(0.5)
                    money = money + 360
                elif valid_choice != win and valid_choice >= 1 and valid_choice <= 39:
                    print("Shocking, you didn't win anything")
                    print()
                    sleep(0.5)
                else:
                    print("That number is not between 1 and 39", "That was your last chance", "You lose", sep="\n")
                    print()
                    sleep(0.5)
    elif money >= 4:
        print("You can't afford this game")
        sleep(0.5)
        choice = input("Enter 'y' if you'd like to play slots one more time. Otherwise press any other key: ")
        if choice == "y":
            money = slots(money, 1)
        else:
            print("Sorry, insufficient funds")
            print()
            sleep(0.5)
    return money

def main():
    money = 100
    while money > 0:
        if money >= 4 and money < 10:
            print("You can only afford to play one game of Slots")
            pick_game = input("Enter 'y' if you would like to play slots: ")
            if pick_game == 'y':
                money = slots (money, 1)
            else:
                break
        elif money >= 10:
            print("Your current balance is $" + str(money), "1. Slots", "2. Roulette", sep='\n' )
            pick_game = input("Please select your choice above or select any other key to exit: ")
            if pick_game == '1':
                num_times = int(input("Select how many times you would like to play the Slots? "))
                money = slots (money, num_times)
            elif pick_game == '2':
                num_times = int(input("Select how many times you would like to play Roulette? "))
                money = roulette (money, num_times)
            else:
                break
        else:
            break
    print("You have managed to crawl out of the casino with $"+str(money))

main()