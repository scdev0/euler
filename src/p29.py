from math import *

def distinct_powers(n):
    '''Return the number of distinct powers a^b for 2 <= a <= n and 2 <= b <= n
    >>> distinct_powers(2)
    1
    >>> distinct_powers(5)
    15
    '''
    length = n - 1
    s = set()
    for a in range(2, n+1):
        for b in range(2, n+1):
            s.add(a ** b)
    return len(s)

def distinct_powers_e(n):
    '''Return the number of distinct powers a^b for 2 <= a <= n and 2 <= b <= n
    >>> distinct_powers_e(2)
    1
    >>> distinct_powers_e(5)
    15
    '''
    length = n - 1
    total = length ** 2
    count = 0
    for a in range(2, n+1):
        for b in range(a+1, n+1):
            if a * log(b) == b * log(a):
                count += 1
    print(count)
    total -= count
    return total
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(distinct_powers(100))