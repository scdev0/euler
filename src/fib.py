def fib_recursive(n):
    '''
    >>> fib_recursive(0)
    1
    >>> fib_recursive(1)
    1
    >>> fib_recursive(3)
    3
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
    
def fib_dy(n):
    '''
    >>> fib_recursive(0)
    1
    >>> fib_recursive(1)
    1
    >>> fib_recursive(3)
    3
    '''
    fib = [0] * (n+1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import time
    #start = time.time()
    #print(fib_recursive(35))
    #end = time.time()
    #print(end-start)
    start = time.time()
    print(len(str(fib_dy(5000))))
    end = time.time()
    print(end-start)
    
    