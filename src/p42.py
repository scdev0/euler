import p22

def triangle_words(filename):
    '''Return the number of triangle words in filename'''
    
    f = open(filename, 'r')
    words = f.readline().split(',')
    words = [word.strip('"') for word in words]
    tri = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666]
    count = 0
    for word in words:
        score = p22.alpha_score(word)
        if score in tri:
            count += 1
    return count

if __name__ == '__main__':
    print(triangle_words('p42_words.txt'))
        