def is_prime(num):
    '''Checks if the number in the parameters is a prime number.
    If the number is prime the function returns True
    Otherwise, the function returns False.
    '''
    for _ in xrange(2, num):  # since 0 and 1 aren't prime
        if (num % _) == 0:
            return False
    return True

#test case
print is_prime(5)  # True
print is_prime(4)  # False
