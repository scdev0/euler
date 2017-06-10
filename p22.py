def alpha_score(s):
    '''Return the score for string s
    >>> alpha_score('A')
    1
    >>> alpha_score('COLIN')
    53
    '''
    s = s.upper()
    total = 0
    for char in s:
        total += ord(char) - 64
    return total
        
def names_scores(filename):
    '''Return the total name scores for the names in filename'''
    f = open(filename, 'r')
    names = f.readline().split(',')
    names = [name.strip('"') for name in names]
    names.sort()
    total = 0
    for i in range(0, len(names)):
        total += alpha_score(names[i]) * (i+1)
    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(names_scores('22_names.txt'))