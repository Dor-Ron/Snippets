#!/usr/bin/env python 

def euclidean(a, b):
    '''finds gcd by means of the Euclidean Algorithm'''
    divisor = min(a, b)
    dividend = max(a, b)
    quotient = dividend / divisor
    remainder = dividend % divisor
    
    while dividend % divisor != 0:
        if remainder == 0:
            gcd = quotient
            print "Your greatest common divisor is %d" % (gcd)
            break
        elif remainder != 0:
            new_dividend = divisor
            new_divisor = dividend
            new_remainder = remainder
            dividend = divisor
            divisor = remainder
            remainder = divisor / remainder
            print "your greatest common divisor is %d" % (new_remainder)
        
#test case
print euclidean(110, 20)
