from math import *
import p3

def ten_thousand_first_prime():
    '''Return the 10001st prime'''
    count = 1 # 2 is the only even prime, start from 3 after and increment by 2
    start = 3
    end = 9999
    while True:
        for i in range(start, end, 2):
            if p3.is_prime(i):
                count += 1
            if count == 10001:
                return i
        # set the next interval
        start = end 
        end = end + 10000

if __name__ == "__main__":
    import time
    start = time.time()
    print(ten_thousand_first_prime())
    end = time.time()
    print(end-start)