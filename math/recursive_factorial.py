#Alternitavely you can import math and use the factorial method ---> math.factorial(x)
#This is my recursive implementation of factorials though

def recursive_factorial(n):
  if n == 0:
    return 1
  else:
    return n * recursive_factorial(n-1)
