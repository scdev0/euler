def is_palindrome(num):
    '''Return True if num is a palindrome. Return False otherwise.
    >>> is_palindrome(1)
    True
    >>> is_palindrome(12)
    False
    >>> is_palindrome(121)
    True
    >>> is_palindrome(1212)
    False
    '''
    str_rep = str(num)
    l = len(str_rep)
    for i in range(0, l//2):
        if str_rep[i] != str_rep[l-i-1]:
            return False
    return True

def product():
    for i in range(999,900,-1):
        for j in range(i,900,-1):
            num = i * j
            if is_palindrome(num):
                return num
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(product())