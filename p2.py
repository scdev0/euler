from math import *

def fib_value(n):
    '''Return the n-th Fibonacci number starting from 1,1,2,...
    >>> fib_value(1)
    1
    >>> fib_value(2)
    1
    >>> fib_value(3)
    2
    '''
    
    return int((((1+sqrt(5))/2) ** n - ((1-sqrt(5))/2) ** n)/sqrt(5))
    
def sum_even_fib():
    '''Return the sum of all even Fibonacci numbers less than 4000000
    '''
    total = 0
    for i in range(0, 34, 3): # loop stops at 34 since the 34th fib value > 4000000
        total += fib_value(i)
    return total
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(sum_even_fib())
