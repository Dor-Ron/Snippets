#!/usr/bin/env python

from logging import basicConfig, info
from random import randint
from re import findall


basicConfig(filename = 'numbers.log', level = "INFO")
num_range = input("Enter the range for the random numbers generated ")

for i in range(100000):
	random_int = randint(0, num_range)
	info(random_int)

num_file = open("numbers.log").read()
num_list = findall(r'\d+', num_file)


def most_common(lst):
    return max(set(lst), key=lst.count)

print '\n'
print most_common(num_list)

