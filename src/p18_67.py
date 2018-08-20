from math import *

def max_path_p18(filename):
    '''Given a file of integers in a triangular shape, return the path with 
    highest total sum from top to bottom.
    >>> max_path_p18('p18_test1.txt')
    75
    >>> max_path_p18('p18_test2.txt')
    170
    >>> max_path_p18('p18_test3.txt')
    390
    '''
    f = open(filename, 'r')
    lst = []
    for line in f:
        lst.append([int(num) for num in line.split()])
    max_total = 0
    for a in range(0, 2):
        for b in range(a, a+2):
            for c in range(b, b+2):
                for d in range(c, c+2):
                    for e in range(d, d+2):
                        for f in range(e, e+2):
                            for g in range(f, f+2):
                                for h in range(g, g+2):                    
                                    for i in range(h, h+2):
                                        for j in range(i, i+2):
                                            for k in range(j, j+2):
                                                for l in range(k, k+2):
                                                    for m in range(l, l+2):
                                                        for n in range(m, m+2):
                                                            #print(0,a,b,c,d,e,f,g,h,i,j,k,l,m,n)
                                                            total = lst[0][0] + lst[1][a] + lst[2][b] + lst[3][c] + lst[4][d] + lst[5][e] + lst[6][f] + lst[7][g] + lst[8][h] + lst[9][i] + lst[10][j] + lst[11][k] + lst[12][l] + lst[13][m] + lst[14][n]
                                                            if max_total < total:
                                                                max_total = total
    return max_total

def max_path_p67(filename):
    '''Given a file of integers in a triangular shape, return the path with 
    highest total sum from top to bottom.
    >>> max_path_p67('p18_test1.txt')
    75
    >>> max_path_p67('p18_test2.txt')
    170
    >>> max_path_p67('p18_test3.txt')
    390
    '''
    f = open(filename, 'r')
    l = []
    for line in f:
        l.append([int(num) for num in line.split()])
    
    for level in range(len(l)-1, 0, -1):
        row = l[level]
        for i in range(0, len(row)-1):
            if row[i] > row[i+1]:
                l[level-1][i] = l[level-1][i] + row[i]
            else:
                l[level-1][i] = l[level-1][i] + row[i+1]
        
    return l[0][0]
    
if __name__ == '__main__':
    import doctest
    #doctest.testmod()
    print(max_path_p67('p67_triangle.txt'))