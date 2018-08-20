from math import *

def sum_factorial(num):
    '''Return the sum of the digits of the factorial of num'''
    return sum([int(n) for n in str(factorial(num))])

if __name__ == '__main__':
    print(sum_factorial(100))