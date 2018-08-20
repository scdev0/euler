if __name__ == "__main__":
    # inefficient
    total = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)
    
    # todo
    # efficient using sum formula