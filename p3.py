from math import *

def is_prime(num):
    '''Return True if num is prime. Return False otherwise
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(9)
    False
    '''
    if num < 2:
        return False
    
    sqr = ceil(sqrt(num+1))
    for i in range(2, sqr):
        if num % i == 0:
            return False
    return True
    
def largest_prime_factor(num):
    '''Return the largest prime factor of num'''
    sqr = ceil(sqrt(num))
    result = 0
    for i in range(2, sqr):
        if num % i == 0:
            if is_prime(i):
                result = i
    return result
                
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(600851475143))