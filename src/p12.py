from math import *

def prime_decomp(num):
    '''Return the prime decomposition of num as a list of ordered tuples (p,e)
    >>> prime_decomp(2)
    [(2, 1)]
    >>> prime_decomp(10)
    [(2, 1), (5, 1)]
    >>> prime_decomp(28)
    [(2, 2), (7, 1)]
    '''
    # when to stop the primes list? can use p7 to generate enough primes
    primes = [2,3,5,7,11,13,17,19,23,29,37,41,47,53,59,61,67,71,73,79,83,89,97]
    result = []
    for p in primes:
        temp = p
        e = 0
        if num % temp == 0:
            while num % temp == 0:
                e += 1
                temp = temp * p
            result.append((p,e))
    return result
    
def num_divisors(num):
    '''Return the number of divisors of num
    >>> num_divisors(2)
    2
    >>> num_divisors(4)
    3
    >>> num_divisors(28)
    6
    '''
    decomp = prime_decomp(num)
    count = 1
    for i in range(0, len(decomp)):
        count = count * (decomp[i][1]+1)
    return count

def triangular_number():
    '''Return the first triangular number with over 500 diviors'''
    
    n = 2
    while True:
        triangle_num = n*(n+1)//2
        count_d = num_divisors(triangle_num)
        if count_d > 500:
            return triangle_num
        n += 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(triangular_number())