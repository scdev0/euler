def sum_digit_powers(num, exp):
    '''Return the sum of digits of num to the power of exp.
    >>> sum_digit_powers(1634, 4)
    1634
    '''
    total = 0
    str_num = str(num)
    for i in range(0, len(str_num)):
        p = int(str_num[i]) ** exp
        total += p
    return total
        
def fifth_powers():
    '''Return the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.'''
    total = 0
    # 9^5 * 6 = 354294, 9^5 * 7 = 413343 -> not possible for 7-digits plus
    for i in range(1000, 354294):
        s = sum([int(n) for n in str(i)])
        if s < 4: # sum of digits < 4 -> not possible to get 4 digits
            continue
        else:
            s_p = sum_digit_powers(i, 5)
            if s_p == i:
                total += i
    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(fifth_powers())