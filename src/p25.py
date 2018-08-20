import fib

def thousand_digit_fib():
    '''Return the index of the first thousand digit fibonacci number'''
    n = 4500
    while True:
        num = fib.fib_dy(n)
        if len(str(num)) == 1000:
            return n
        n += 1
        
if __name__ == '__main__':
    print(thousand_digit_fib())