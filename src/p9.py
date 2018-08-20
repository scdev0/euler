def special_py_triplet():
    # more efficient solution would be applying the general forms of pythagoren triples
    for a in range(1, 500):
        b = (500000-1000*a)/(1000-a)
        # find the integer solution
        if b == int(b):
            c = 1000-a-b
            return a*b*c
    
if __name__ == "__main__":
    import time
    start = time.time()
    print(special_py_triplet())
    end = time.time()
    print(end-start)