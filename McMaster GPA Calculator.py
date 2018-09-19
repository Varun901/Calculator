from operator import mul

def sum_func(units, grades):
    """ For product below you can also use the following commands:
1. [a*b for a,b in zip(a,b)]

2. import numpy as np
    product = np.multiply(units,grades)
"""
    product = map(mul,units,grades)
    sum_product = sum(product)
    return sum_product

def num_func(units):
    total_units = sum(units)
    return total_units

def avg_func(sum_product, total_units):
    cumulative_GPA = sum_product / total_units
    return cumulative_GPA

def main():
    course_units = [int(x) for x in input("Enter your course units, each one separated by a space: ").split()]
    course_grades = [int(x) for x in input("Enter your course grades in the same order as your units, each one separated by a space: ").split()]
    sum_product = sum_func(course_units,course_grades)
    total_units = num_func(course_units)
    gpa = avg_func(sum_product, total_units)
    print ("The student's GPA is %.1f." % (gpa))
main()