#You can use the factorial method of the math module as an alternative
#This is my iterative implementation for the factorial function

def iterative_factorial(n):
    result = 1
    for i in xrange(2, n+1):
        result *= i
    return result
