# File: Area_Calculator.py
# This program calculates area for Squares, Rectangles, Circles, Triangles, Ellipses, Parallelograms, Trapezoids
# In this program the user is able to choose the calculation they need and input the values
# In order to add a slight delay in the program response a sleep function was added
from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()


def main():
    print ("The calculator is starting up...")
    print('%02d/%02d/%04d  %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
    sleep(1)
    print ("")
    print("Area Calculator")
    print("This program calculates area for... ")
    print("Squares, Rectangles, Circles, Triangles, Ellipses, Parallelograms, and Trapezoids!")
    print ("")
    hint = "Don't forget to include the correct units! \nExiting... "

    option = input("What shape do you want to calculate the area for? ")

    if option == 'C' or option == 'c' or option == "Circle" or option == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = pi * radius ** 2
        sleep(1)
        print("Area: %.2f. \n%s" % (area, hint))
    elif option == 'T' or option == "t" or option == "Triangle" or option == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = (0.5) * base * height
        sleep(1)
        print("Area: %.2f. \n%s" % (area, hint))
    elif option == 'Trap' or option == 'trap' or option == 'Trapezoid' or option == 'trapezoid':
        height = float(input("Enter the height: "))
        long_base = float(input('Enter the length of the longer base: '))
        short_base = float(input('Enter the length of the short base: '))
        area = height * (0.5 * (long_base + short_base))
        sleep(1)
        print("Area: %.2f. \n%s" % (area, hint))
    elif option == "Square" or option == "square" or option == "S" or option == "s":
        side = float(input("Enter the side length: "))
        area = side ** 2
        sleep (1)
        print("Area: %.2f. \n%s" % (area, hint))
    elif option == "Rectangle" or option == "rectangle" or option == "R" or option == "r":
        long_side = float(input("Enter the length of the longer side length: "))
        short_side = float(input("Enter the length of the shorter side: "))
        area = long_side * short_side
        sleep(1)
        print("Area: %.2f. \n%s" % (area, hint))
    elif option == "Parallelogram" or option == "parallelogram" or option == "P" or option == "p":
        height = float(input("Enter the height: "))
        base = float(input("Enter the base: "))
        area = base * height
        sleep(1)
        print("Area: %.2f. \n%s" % (area, hint))
    elif option == "Ellipse" or option == "ellipse" or option == "E" or option == "e":
        semi_major_axis = float(input("Enter the length of the semi-major axis: "))
        semi_minor_axis = float(input("Enter the length of the semi_minor axis: "))
        area = pi * semi_major_axis * semi_minor_axis
        sleep(1)
        print("Area: %.2f. \n%s" % (area, hint))
    else:
        print("You need to choose a shape!")
        sleep(1)
        main()
main()