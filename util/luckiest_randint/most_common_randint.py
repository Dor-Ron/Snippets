#!/usr/bin/env python

from logging import basicConfig, info
from random import randint
from re import findall
from os import system


basicConfig(filename = 'numbers.log', level = "INFO")
num_range = input("Enter the range for the random numbers generated ")

for loop in range(100000):
    random_int = randint(0, num_range)
    info(random_int)

num_file = open("numbers.log").read()
num_list = findall(r'\d+', num_file)


def most_common(lst):
    return max(set(lst), key=lst.count)

#in order to allow the script to be run again under the same file name
def delete_log(file):
    system("rm %s" % file)

if __name__ == "__main__":
    print  most_common(num_list)
    delete_log("numbers.log")

