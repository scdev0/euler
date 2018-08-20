import p3
import time

def primes(num):
    '''Return a list of primes < num
    >>> primes(2)
    []
    >>> primes(3)
    [2]
    >>> primes(10)
    [2, 3, 5, 7]
    '''
    l = []
    for i in range(2, num):
        if p3.is_prime(i):
            l.append(i)
    return l

def rotations(num):
    '''Return a list of the rotations of num in increasing order
    >>> rotations(2)
    [2]
    >>> rotations(10)
    [1, 10]
    >>> rotations(197)
    [197, 719, 971]
    '''
    l = [num]
    str_num = str(num)
    new = str_num
    for i in range(len(str_num)-1, 0, -1):
        new = new[-1] + new[0:-1]
        l.append(int(new))
    l.sort()
    return l
    
def circular_primes(num):
    '''Return the number of circular primes < num
    >>> circular_primes(2)
    0
    >>> circular_primes(3)
    1
    >>> circular_primes(100)
    13
    '''
    l = primes(num)
    count = 0
    for prime in l:
        rs = rotations(prime)
        for rotation in rs:
            if not p3.is_prime(rotation):
                break
        else:
            count += 1
    return count
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(circular_primes(1000000))