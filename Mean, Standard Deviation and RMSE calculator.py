import math
import statistics
from time import sleep

def calc_mean(datalist):
    mean = sum(datalist)/len(datalist)
    return mean

def calc_sd(datalist):
    mean = calc_mean(datalist)
    stdev = math.sqrt(sum([(x - mean)**2 for x in datalist])/(len(datalist)-1))
    return stdev

def calc_rmse(datalist1, datalist2):
    differences = [x - y for x, y in zip (datalist1, datalist2)]
    rmse = math.sqrt(sum([x**2 for x in differences]))
    return rmse

def main():
    predicted = [int(x) for x in input("Enter your predicted dataset: ").split()]
    observed = [int(x) for x in input("Enter your observed dataset: ").split()]
    mean_p = calc_mean(predicted)
    stdev_p = calc_sd(predicted)
    mean_o = calc_mean(observed)
    stdev_o = calc_sd(observed)
    rmse = calc_rmse(predicted, observed)
    print("The mean of the predicted dataset is %.2f." % (mean_p))
    sleep(1)
    print("The standard deviation of the predicted data set is %.2f." % (stdev_p))
    sleep(1)
    print("The mean of the observed dataset is %.2f." % (mean_o))
    sleep(1)
    print("The standard deviation of the observed data set is %.2f." % (stdev_o))
    sleep(1)
    print("The RMSE of the datasets is %.2f." % (rmse))

    stdev1 = statistics.stdev(predicted)
    stdev2 = statistics.stdev(observed)
    print(stdev_p == stdev1)
    print(stdev_o == stdev2)
main()
