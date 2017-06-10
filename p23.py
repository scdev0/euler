import p21
import time

def abundant_numbers(num):
    '''Return a list of abundant numbers upto num in increasing order
    >>> abundant_numbers(11)
    []
    >>> abundant_numbers(12)
    [12]
    >>> abundant_numbers(40)
    [12, 18, 20, 24, 30, 36, 40]
    '''
    lst = []
    for i in range(12, num+1): # 12 is the first abundant number
        if p21.sum_proper_divisors(i) > i:
            lst.append(i)
    return lst
    
def sum_abundant_numbers(num):
    '''Return the sum of all numbers that can't be written as the sum of two
    abundant numbers upto num
    >>> sum_abundant_numbers(23)
    276
    >>> sum_abundant_numbers(24)
    276
    >>> sum_abundant_numbers(50)
    891
    >>> sum_abundant_numbers(100)
    2766
    '''
    l = abundant_numbers(num)
    new_l = set()
    i = 0
    found = False
    while i < len(l) and not found:
        for j in range(i, len(l)):
            if l[i] * 2 > num:
                found = True
                break
            elif l[i] + l[j] > num:
                break
            else:
                s = l[i] + l[j]
                new_l.add(s)
        i += 1
    new_l = list(new_l)
    new_l.sort()
    
    for i in range(0, len(new_l)):
        if new_l[i] > num:
            break
    new_l = new_l[0:i+1]
    total = sum(list(range(num+1))) - sum(new_l)
    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    start = time.time()
    print(sum_abundant_numbers(20161)) # 20161 is the upper limit of numbers 
                                        # that can't be written as required
    end = time.time()
    print(end-start)