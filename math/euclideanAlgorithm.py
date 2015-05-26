def euclidean(a, b):
    if a < b:
        divisor = a
        dividend = b
    elif b < a:
        divisor = b
        dividend = a
    else:
        print "There's no point in doing this."

#now that we know which is the divisor and which is the dividend we can
#begin dividing and analyzing them.
    while dividend % divisor != 0:
        quotient = dividend / divisor
        remainder = dividend % divisor
        if remainder == 0:
            gcd = quotient
            print "Your greatest common divisor is %d" % (gcd)
            break;
        elif remainder != 0:
            new_dividend = divisor
            new_divisor = dividend
            new_remainder = remainder
            dividend = divisor
            divisor = remainder
            remainder = divisor/remainder
            print "your greatest common divisor is %d" % (new_remainder)
        else:
            pass

#test case
print euclidean(110,20)
