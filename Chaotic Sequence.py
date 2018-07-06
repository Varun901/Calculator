# File: chaos.py
# a simple program illustrating chaotic behaviour


def main():
    print("This program illustrates chaotic behaviour")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n = eval(input("How many numbers should I print: "))
    print("x", '\t \t', "y")
    print("----------------------")
    for i in range (n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("%.2f" % x,  '\t',"%.2f" % y)

main()
