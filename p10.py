from math import *
import p3

# brute-force
def sum_prime(num):
    '''Return sum of primes < num
    >>> sum_prime(2)
    2
    >>> sum_prime(10)
    17
    '''
    total = 0
    for i in range(2, num+1):
        if p3.is_prime(i):
            total += i
    return total

# using a sieve
def sum_prime_sieve(num):
    '''Return sum of primes < num'''
    crossed = [0] * num
    value = 3
    total = 2
    while value <= num:
        if crossed[value] == 0: # value hasn't been crossed out yet
            total += value
            i = value
            while i < num: # cross out all the multiples of value
                crossed[i] = 1
                i += value
        value += 2
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import time
    #start = time.time()
    #print(sum_prime(2000000))
    #end = time.time()
    #print(end-start)
    start = time.time()
    print(sum_prime_sieve(2000000))
    end = time.time()
    print(end-start)  