def fibi(n):
    c, v = 0, 1
    for i in range(n-1): #don't need last iteration, more efficient this way
        c, v = v, (c + v)
    return v #instead of c if i used n in place of n-1
