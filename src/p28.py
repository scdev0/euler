def spiral(n):
    '''Return the sum of the diagonals in the nxn spiral formed starting from 1
    >>> spiral(1)
    1
    >>> spiral(3)
    25
    >>> spiral(5)
    101
    '''
    num = 1
    step = 2
    total = 1
    for i in range(3, n+1, 2):
        for j in range(0, 4):
            num += step
            total += num
        step += 2
            
    return total

def spiralo(n):
    '''Return the sum of the diagonals in the nxn spiral formed starting from 1
    >>> spiralo(1)
    1
    >>> spiralo(3)
    25
    >>> spiralo(5)
    101
    '''
    c = 1
    skip = 1
    skipc = 0
    total = 1
    while (c<n**2):
        c+=skip+1
        total += c
        skipc += 1
        if skipc == 4:
            skipc = 0
            skip+=2
        
    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(spiral(1001))
    print(spiralo(1001))