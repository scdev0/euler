# slow brute-force

def collatz_length(num):
    '''Return the length of the collazt sequence starting from num
    >>> collatz_length(1)
    0
    >>> collatz_length(4)
    2
    >>> collatz_length(27)
    111
    '''
    n = num
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count += 1
    return count

def longest_collatz():
    '''Return the number under 1 million that has the longest collatz sequence'''
    max_length = 0
    number = 0
    for i in range(500001, 1000000, 2):
        length = collatz_length(i)
        if max_length < length:
            max_length = length
            number = i
    return number
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import time
    start = time.time()
    print(longest_collatz())
    end = time.time()
    print(end-start)    
        
    