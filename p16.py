def get_sum(num):
    '''Return the sum of the digits in num'''
    l = list(str(num))
    l = [int(n) for n in l]
    return sum(l)

if __name__ == '__main__':
    print(get_sum(2 ** 1000))
    