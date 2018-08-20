import p4

def double_base_palindrome():
    '''Return the sum of all numbers, less than one million, which are 
    palindromic in base 10 and base 2.'''
    total = 0
    for i in range(1, 1000000, 2): # palindromic numbers in base 2 must be odd
        i2 = "{0:b}".format(i)
        if p4.is_palindrome(str(i)) and p4.is_palindrome(i2):
            total += i
            
    return total
    
if __name__ == '__main__':
    print(double_base_palindrome())