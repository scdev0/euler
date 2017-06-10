def self_powers():
    '''Return the last ten digits of the series 1^1 + 2^2 +...+ 1000^1000'''
    total = 0
    for i in range(1, 1000):
        total += i ** i
        
    # to get last 10 digits, mod by 10 ^ 10
    return total % (10 ** 10)

if __name__ == '__main__':
    print(self_powers())