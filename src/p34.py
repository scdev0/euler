from math import *

def sum_digit_factorials():
    '''Return the sum of all numbers which are equal to the sum of the factorial
    of their digits.'''
    total = 0
    for i in range(10, 2540160):
        s = sum([factorial(int(n)) for n in str(i)]) # can preset factorials to optimize
        if s == i:
            total += i
    return total

if __name__ == '__main__':
    print(sum_digit_factorials())