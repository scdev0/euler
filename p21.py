def sum_proper_divisors(num):
    '''Return the sum of the proper divisors of num
    >>> sum_proper_divisors(2)
    1
    >>> sum_proper_divisors(220)
    284
    >>> sum_proper_divisors(284)
    220
    '''
    if num == 1:
        return 0
    
    total = 1
    for i in range(2, int(num ** (0.5))+1):
        if num % i == 0:
            # if i is a divisor of num then so is num / i
            total += i
            if i != num // i: # check for perfect squares
                total += num // i
    return total
    
def sum_amicable_numbers(num):
    '''Return the sum of all amicable numbers below num
    >>> sum_amicable_numbers(300)
    504
    >>> sum_amicable_numbers(3000)
    8442
    '''
    total = 0
    for i in range(2, num):
        sum_d1 = sum_proper_divisors(i)
        sum_d2 = sum_proper_divisors(sum_d1)
        if sum_d2 == i and sum_d1 != i:
            total = total + sum_d1 + sum_d2
    return total // 2

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    import time
    start = time.time()
    print(sum_amicable_numbers(10000))
    end = time.time()
    print(end-start)
            
    