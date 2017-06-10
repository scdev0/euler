def num_paths(r, c):
    '''Return the number of paths only using right/down in a grid of size rxc
    >>> num_paths(1,1)
    2
    >>> num_paths(2,2)
    6
    >>> num_paths(2,3)
    10
    '''
    g = {}
    # initial grid with 'zero' row
    for i in range(0, c+1):
        g[(0,i)] = 1
    
    # initial grid with 'zero' column
    for i in range(0, c+1):
        g[(i,0)] = 1

    for i in range(1, r+1):
        for j in range(1, c+1):
            g[(i,j)] = g[(i,j-1)] + g[(i-1,j)]

    return g[(r,c)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import time
    start = time.time()
    print(num_paths(20,20))
    end = time.time()
    print(end-start)    
    
                