def fibonacci(n):
    c, v = 0, 1
    for i in xrange(n-1): 
        c, v = v, (c + v)
    return v 
