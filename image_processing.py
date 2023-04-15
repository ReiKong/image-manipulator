import doctest

def is_valid_image(img_matrix):
    ''' (list<list>) -> bool
    Returns True if img_matrix is composed of only integers,
    has sublists of the same length, and has values only between 0 and 255.
    
    >>> is_valid_image([[3, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    
    >>> is_valid_image([['3', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
    True
    
    >>> is_valid_image([[1]])
    True
    
    >>> is_valid_image([['3', '2', '333'], ['4', '5', '6'], ['7', '8', '9']])
    False
    
    >>> is_valid_image([[1, 2, 7], [1, 4, 6], [1, 3]])
    False
    
    >>> is_valid_image([[2, 3, 7], [1, 5, 8], [1, 'gfds', 4]])
    False
    
    >>> is_valid_image([[9, 7, 7], [1, '3x0', 6]])
    False
    
    >>> is_valid_image([[1, 2, 74893], [1, 4, 6], [9, 2, 4]])
    False
    
    >>> is_valid_image([[[1], [2], [74893]], [1, 4, 6], [9, 2, 4]])
    False
    
    >>> is_valid_image([[True, 2, 1], [1, 4, 6], [9, 2, 4]])
    False
    '''
    
    num_row = len(img_matrix)
    length = len(img_matrix[0])
    
    for r in range(num_row):
        num_col = len(img_matrix[r])
        
        if len(img_matrix[r]) != length:
            return False
        
        for c in range(num_col):
            elem = img_matrix[r][c]
            
            if type(elem) == str and elem.isdecimal():
                elem = int(elem)
            elif type(elem) != int:
                return False
            
            if not(0 <= elem <= 255):
                return False

    return True


def is_valid_compressed_image(img_matrix):
    ''' (list<list>) -> bool
    Returns True if img_matrix contains strings in the form 'AxB',
    A is an integer between 0 and 255, B is a natural number, and
    the sum of all B values in one row is the same in each row.
    
    >>> is_valid_compressed_image([['0x5', '200x2'], ['111x7']])
    True
    
    >>> is_valid_compressed_image([['5x7', '9x3'], ['5x10'], ['4x6', '8x4']])
    True
    
    >>> is_valid_compressed_image([[3, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    
    >>> is_valid_compressed_image([['20x4', '4x2'], ['20x3']])
    False
    
    >>> is_valid_compressed_image([[0], [0, 0]])
    False
    
    >>> is_valid_compressed_image([[True], [0, 0]])
    False
    
    >>> is_valid_compressed_image([[[0], [1]], [0, 0]])
    False
    
    >>> is_valid_compressed_image([['20x2000', '200x2'], ['50x7']])
    False
    
    >>> is_valid_compressed_image([['20xx2000', '200x2'], ['50x7']])
    False
    
    >>> is_valid_compressed_image([['ab3xc3', 'bx2'], ['50x7']])
    False
    
    >>> is_valid_compressed_image([['0x@', '200x2'], ['111x7']])
    False
    
    >>> is_valid_compressed_image([['x', 'x2'], ['111x7']])
    False
    '''
    
    num_row = len(img_matrix)
    b_sum_list = []
    
    for r in range(num_row):
        num_col = len(img_matrix[r])
        b_sum = 0
        for c in range(num_col):
            elem = img_matrix[r][c]
            
            if type(elem) != str or elem.count('x') != 1:
                return False
            
            elem = elem.split('x')
            a = elem[0]
            b = elem[1]
            
            if not(a.isdecimal() and b.isdecimal()):
                return False
            
            b_sum += int(b)
        
            if not (0 <= int(a) <= 255 and 0 < int(b)):
                return False
        
        # checks if the sum of b values in each row are the same
        b_sum_list.append(b_sum)
        valid_sum = b_sum_list.count(b_sum_list[0]) == len(b_sum_list)
    
    return valid_sum


def read_image(fobj):
    ''' (str) -> list<list<str>>
    Returns a file object as a matrix.
    
    >>> fobj = open('comp.pgm', 'r')
    >>> read_image(fobj)
    [['P2'], ['24', '7'], ['255'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '51', '51', '51', '51', '51', '0', '119', '119', '119', '119', '119', '0', '187', '187', '187', '187', '187', '0', '255', '255', '255', '255', '0'], ['0', '51', '0', '0', '0', '0', '0', '119', '0', '0', '0', '119', '0', '187', '0', '187', '0', '187', '0', '255', '0', '0', '255', '0'], ['0', '51', '0', '0', '0', '0', '0', '119', '0', '0', '0', '119', '0', '187', '0', '187', '0', '187', '0', '255', '255', '255', '255', '0'], ['0', '51', '0', '0', '0', '0', '0', '119', '0', '0', '0', '119', '0', '187', '0', '187', '0', '187', '0', '255', '0', '0', '0', '0'], ['0', '51', '51', '51', '51', '51', '0', '119', '119', '119', '119', '119', '0', '187', '0', '187', '0', '187', '0', '255', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]
    >>> fobj.close()
    
    >>> fobj = open('comp.pgm.compressed', 'r')
    >>> read_image(fobj)
    [['P2C'], ['24', '7'], ['255'], ['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> fobj.close()
    
    >>> fobj = open('comp3.pgm', 'r')
    >>> read_image(fobj)
    [['P2'], ['9', '4'], ['255'], ['0', '0', '0', '0', '119', '0', '0', '0', '119'], ['0', '0', '0', '0', '119', '0', '0', '0', '119'], ['51', '51', '51', '0', '119', '119', '119', '119', '119'], ['0', '0', '0', '0', '0', '0', '0', '0', '0']]
    >>> fobj.close()
    '''
    
    img_matrix = []
    
    for line in fobj:
        img_matrix.append(line.split())
    
    return img_matrix


def is_valid_details(img_matrix, img_type):
    ''' (<list<list<str>>>, str) -> bool
    Returns True if img_matrix[0][0] corresponds with its file type
    ('P2' for regular PGM image, 'P2C' for compressed PGM image) and
    if img_matrix[2][0] is '255'.
    Returns False if otherwise.
    
    >>> img_matrix = [['P2'], ['24', '7'], ['255'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> img_type = 'reg'
    >>> is_valid_details(img_matrix, img_type)
    True

    >>> img_matrix = [['P2C'], ['24', '7'], ['255'], ['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> img_type = 'comp'
    >>> is_valid_details(img_matrix, img_type)
    True

    >>> img_matrix = [['P2'], ['24', '7'], ['250'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> img_type = 'reg'
    >>> is_valid_details(img_matrix, img_type)
    False
    
    >>> img_matrix = [['P2X'], ['24', '7'], ['255'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> img_type = 'reg'
    >>> is_valid_details(img_matrix, img_type)
    False
    '''
    
    if img_type == 'reg':
        valid_type = img_matrix[0][0] == 'P2'
    else:
        valid_type = img_matrix[0][0] == 'P2C'
    
    valid_max_value = img_matrix[2][0] == '255'
    
    return valid_type and valid_max_value


def load_regular_image(filename):
    ''' (str) -> list<list<int>>
    Opens filename and returns as an image matrix.
    If, during or after loading, the image matrix is not in PGM format,
    an AssertionError is raised.
    
    >>> load_regular_image('comp.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> load_regular_image('comp.txt')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    >>> load_regular_image('comp.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    
    >>> load_regular_image('invalid.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    
    >>> load_regular_image('invalid2.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    
    >>> load_regular_image('invalid3.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    
    >>> load_regular_image('invalid4.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    
    >>> load_regular_image('invalid5.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    
    >>> load_regular_image('invalid6.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    
    >>> load_regular_image('invalid7.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    
    >>> load_regular_image('empty.pgm')
    Traceback (most recent call last):
    AssertionError: Input must not be empty.
    
    >>> load_regular_image('empty2.pgm')
    Traceback (most recent call last):
    AssertionError: Input must not be empty.
    '''
    
    fobj = open(filename, 'r')
    img_matrix = read_image(fobj)
    fobj.close()
    
    if len(img_matrix) <= 3:
        raise AssertionError('Input must not be empty.')
    
    valid_image = is_valid_details(img_matrix, 'reg') and is_valid_image(img_matrix[3:])
    
    if not(valid_image):
        raise AssertionError('Input must be in PGM image format.')
    
    num_row = int(img_matrix[1][1])
    num_col = int(img_matrix[1][0])
    valid_num_row = num_row == len(img_matrix) - 3
    valid_num_col = num_col == len(img_matrix[3])
    
    if not(valid_num_row and valid_num_col):
        raise AssertionError('Input must be in PGM image format.')
    
    for r in range(3, num_row + 3):
        for c in range(num_col):
            img_matrix[r][c] = int(img_matrix[r][c])
    
    return img_matrix[3:]


def load_compressed_image(filename):
    ''' (str) -> list<list<str>>
    Opens  filename and returns as an image matrix.
    If, during or after loading, the image matrix is not
    in compressed PGM format, an AssertionError is raised.
    
    >>> load_compressed_image('comp.pgm.compressed')
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> load_compressed_image('comp.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in a valid compressed PGM image format.
    
    >>> load_compressed_image('invalid.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in a valid compressed PGM image format.
    
    >>> load_compressed_image('invalid2.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in a valid compressed PGM image format.
    
    >>> load_compressed_image('invalid3.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in a valid compressed PGM image format.
    
    >>> load_compressed_image('invalid4.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in a valid compressed PGM image format.
    
    >>> load_compressed_image('invalid2.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: The number of rows and columns of image matrix\'s contents must match the number of rows and columns specified in the second line of the file.
    
    >>> load_compressed_image('invalid3.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: The number of rows and columns of image matrix\'s contents must match the number of rows and columns specified in the second line of the file.
    
    >>> load_compressed_image('empty.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: Input must not be empty.
    
    >>> load_compressed_image('empty2.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: Input must not be empty.
    '''
    
    fobj = open(filename, 'r')
    img_matrix = read_image(fobj)
    fobj.close()
    
    if len(img_matrix) <= 3:
        raise AssertionError('Input must not be empty.')
    
    valid_image = is_valid_details(img_matrix, 'comp') and is_valid_compressed_image(img_matrix[3:])
    
    if not(valid_image):
        raise AssertionError('Input must be in a valid compressed PGM image format.')
    
    num_row = int(img_matrix[1][1])
    num_col = int(img_matrix[1][0])
    valid_num_row = num_row == len(img_matrix) - 3
    b_sum = 0
    
    for c in range(len(img_matrix[3])):
        elem = img_matrix[3][c].split('x')
        b = elem[1]
        b_sum += int(b)
    
    valid_num_col = num_col == b_sum
    
    if not(valid_num_row and valid_num_col):
        raise AssertionError('The number of rows and columns of image matrix\'s contents must match the number of rows and columns specified in the second line of the file.')
    
    return img_matrix[3:]


def load_image(filename):
    ''' (str) -> list<list>
    If file is a compressed PGM image, calls load_compressed_image(filename)
    and returns a compressed PGM image matrix.
    If file is a PGM image, calls load_regular_image(filename)
    and returns a PGM image matrix.
    
    >>> load_image('comp.pgm.compressed')
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> load_image('comp.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    >>> load_image('test2.txt')
    [['0x5', '200x2'], ['111x7']]

    >>> load_image('invalid.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: Input must be in a valid compressed PGM image format.
    
    >>> load_image('invalid.pgm')
    Traceback (most recent call last):
    AssertionError: Input must be in PGM image format.
    '''
    
    fobj = open(filename, 'r')
    file_type = read_image(fobj)
    file_type = file_type[0][0]
    
    if file_type == 'P2C':
        img = load_compressed_image(filename)
    elif file_type == 'P2':
        img = load_regular_image(filename)
    else:
        raise AssertionError('File must be a PGM image or compressed PGM image.')

    return img


def save_regular_image(img_matrix, filename):
    ''' (list<list>, str) -> NoneType
    Saves nested_list to a file with filename.
    If nested_list is not a valid PGM matrix, raises an AssertionError.
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], 'test.pgm')
    >>> fobj = open('test.pgm', 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> fobj.close()
    >>> image = [[0]*10, [255]*10, [0]*10]
    >>> image2 = load_image('test.pgm')
    >>> image == image2
    True
    '''

    if not(is_valid_image(img_matrix)):
        raise AssertionError('Nested list must be a matrix in PGM image format.')
    
    num_row = len(img_matrix)
    num_col = len(img_matrix[0])
    img = 'P2\n' + str(num_col) + ' ' + str(num_row) + '\n255\n'
    
    for r in range(num_row):
        img_row = ' '
        for c in range(num_col):
            img_matrix[r][c] = str(img_matrix[r][c])
        img_row = img_row.join(img_matrix[r])
        img = img + img_row + '\n'
    
    fobj = open(filename, 'w')
    fobj.write(img)
    fobj.close()


def get_num_col_compressed_img(img_matrix):
    ''' (<list<list>>) -> int
    Returns the sum of all b values in the first row of img_matrix.
    
    >>> get_num_col_compressed_img([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    5
    
    >>> get_num_col_compressed_img([['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x29', '239x1'], ['255x27', '223x1', '95x1', '15x1'], ['255x25', '239x1', '95x1', '0x3'], ['255x24', '143x1', '15x1', '0x4'], ['255x22', '207x1', '47x1', '0x5', '14x1'], ['255x21', '159x1', '15x1', '0x4', '14x1', '95x1', '115x1']])
    30
    
    >>> get_num_col_compressed_img([['3x3', '4x3'], ['5x6']])
    6
    '''
    
    first_row = img_matrix[0]
    b_list = []
    
    for c in range(len(first_row)):
        elem = first_row[c].split('x')
        b = int(elem[1])
        b_list.append(b)
        
    b_sum = 0
    
    for i in range(len(b_list)):
        b_sum += b_list[i]
    
    return b_sum


def save_compressed_image(img_matrix, filename):
    ''' (<list<list>>, str) -> NoneType
    Saves img_matrix as filename.
    If img_matrix is not a valid compressed PGM
    image matrix, raise an AssertionError.
    
    >>> save_compressed_image([['0x5', '200x2'], ['111x7']], 'test.pgm.compressed')
    >>> fobj = open('test.pgm.compressed', 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_compressed_image([['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']], 'test2.pgm.compressed')
    >>> fobj = open('test2.pgm.compressed', 'r')
    >>> fobj.read()
    'P2C\\n24 7\\n255\\n0x24\\n0x1 51x5 0x1 119x5 0x1 187x5 0x1 255x4 0x1\\n0x1 51x1 0x5 119x1 0x3 119x1 0x1 187x1 0x1 187x1 0x1 187x1 0x1 255x1 0x2 255x1 0x1\\n0x1 51x1 0x5 119x1 0x3 119x1 0x1 187x1 0x1 187x1 0x1 187x1 0x1 255x4 0x1\\n0x1 51x1 0x5 119x1 0x3 119x1 0x1 187x1 0x1 187x1 0x1 187x1 0x1 255x1 0x4\\n0x1 51x5 0x1 119x5 0x1 187x1 0x1 187x1 0x1 187x1 0x1 255x1 0x4\\n0x24\\n'
    >>> fobj.close()
    '''

    if not(is_valid_compressed_image(img_matrix)):
        raise AssertionError('Nested list must be a matrix in compressed PGM image format.')
    
    num_row = len(img_matrix)
    num_col = get_num_col_compressed_img(img_matrix)
    img = 'P2C\n' + str(num_col) + ' ' + str(num_row) + '\n255\n'
    
    for r in range(num_row):
        img_row = ' '
        img_row = img_row.join(img_matrix[r])
        img = img + img_row + '\n'
        
    fobj = open(filename, 'w')
    fobj.write(img)
    fobj.close()


def save_image(img_matrix, filename):
    '''(<list<list>>) -> NoneType
    Saves img_matrix as filename.
    If img_matrix is not a valid compressed PGM image matrix
    or PGM image matrix, raise an AssertionError.
    
    >>> save_image([['0x5', '200x2'], ['111x7']], 'test2.pgm.compressed')
    >>> fobj = open('test2.pgm.compressed', 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_image([['0x5', '200x2'], ['111x7']], 'test2.txt')
    >>> fobj = open('test2.txt', 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    '''
    
    if type(img_matrix[0][0]) == int:
        save_regular_image(img_matrix, filename)
    elif type(img_matrix[0][0]) == str:
        save_compressed_image(img_matrix, filename)
    else:
        raise AssertionError('The elements of the image matrix must either be strings or integers.')


def invert(img_matrix):
    ''' (<list<list>>) -> <list<list>>
    Returns a nested list where each element of img_matrix is subtracted from 255.
    Raises an AssertionError if the input matrix is not a valid PGM image matrix.
    
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> image == [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    True
    
    >>> img = [[3, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> invert(img)
    [[252, 253, 252], [251, 250, 249], [248, 247, 246]]
    >>> img == [[3, 2, 3], [4, 5, 6], [7, 8, 9]]
    True
    
    >>> image = [[0, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    Traceback (most recent call last):
    AssertionError: Nested list must be a matrix in PGM image format.
    
    >>> image = [[0, 261, 250], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    Traceback (most recent call last):
    AssertionError: Nested list must be a matrix in PGM image format.
    '''
    
    if not(is_valid_image(img_matrix)):
        raise AssertionError('Nested list must be a matrix in PGM image format.')
    
    num_row = len(img_matrix)
    num_col = len(img_matrix[0])
    inv_img_matrix = []
    
    for r in range(num_row):
        sub_inv_img_matrix = []
        for c in range(num_col):
            num = 255 - img_matrix[r][c]
            sub_inv_img_matrix.append(num)
        inv_img_matrix.append(sub_inv_img_matrix)
    
    return inv_img_matrix


def flip(img_matrix, direction):
    ''' (<list<list>>) -> <list<list>>
    If direction == 'h', returns  the elements of each sublist in img_matrix reversed.
    If direction is not 'h', returns the order of sublists in img_matrix reversed.
    Raises an AssertionError if the input matrix is not a valid PGM image matrix.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    
    >>> image = [[1, 2, 3, 4], [0, 0, 5], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    Traceback (most recent call last):
    AssertionError: Input matrix must be in PGM image format.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    
    >>> image = [[1, 2, 3, 4, 'a'], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: Input matrix must be in PGM image format.
    
    >>> image = [[1, 2, 3, 4], [0, 0, 5], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: Input matrix must be in PGM image format.
    '''
    
    if not(is_valid_image(img_matrix)):
        raise AssertionError('Input matrix must be in PGM image format.')
    
    num_row = len(img_matrix)
    new_img_matrix = []
    
    if direction == 'h':
        for r in range(num_row):
            sub_img_matrix = img_matrix[r][::-1]
            new_img_matrix.append(sub_img_matrix)
    else:
        for r in range(num_row):
            new_img_matrix = img_matrix[::-1]
            
    return new_img_matrix


def flip_horizontal(img_matrix):
    ''' (<list<list>>) -> <list<list>>
    Returns  the elements of each sublist in img_matrix reversed.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    
    >>> image = [[1, 2, 3, 4, 'a'], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: Input matrix must be in PGM image format.
    
    >>> image = [[1, 2, 3, 4], [0, 0, 5], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: Input matrix must be in PGM image format.
    '''
    
    new_img_matrix = flip(img_matrix, 'h')
    
    return new_img_matrix
    
    
def flip_vertical(img_matrix):
    ''' (<list<list>>) -> <list<list>>
    Returns the order of sublists in img_matrix reversed.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    
    >>> image = [[1, 2, 3, 4], [0, 0, 5], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    Traceback (most recent call last):
    AssertionError: Input matrix must be in PGM image format.
    '''
    
    new_img_matrix = flip(img_matrix, 'v')
    
    return new_img_matrix


def crop(img_matrix, top_left_row, top_left_col, num_row, num_col):
    ''' (list<list>) -> <list<list>>
    Returns a nested list of integers at indices top_left_row to num_row
    and top_left_col to num_col of img_matrix.

    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 1, 2, 2, 1)
    [[6], [10]]
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 0, 0, 3, 4)
    [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]
    '''
    
    if not(is_valid_image(img_matrix)):
        raise AssertionError('Input matrix must be in PGM image format.')
    
    num_row = top_left_row + num_row
    num_col = top_left_col + num_col
    valid_num_row = num_row <= len(img_matrix)
    valid_num_col = num_col <= len(img_matrix[0])
    
    if not (valid_num_row and valid_num_col):
        raise AssertionError('The dimensions given must be valid.')
    
    new_img_matrix = []
    
    for r in range(top_left_row, num_row):
        sub_new_img_matrix = []
        for c in range(top_left_col, num_col):
            sub_new_img_matrix.append(img_matrix[r][c])
        new_img_matrix.append(sub_new_img_matrix)

    return new_img_matrix


def find_end_of_repetition(int_list, ind, target_num):
    ''' (<list<int>>) -> int
    Looks through int_list starting after ind.
    Returns the index of the last consecutive occurrence of the target_num.
    
    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
    4
    
    >>> find_end_of_repetition([1, 2, 3, 4, 5, 6, 7], 6, 7)
    6
    
    >>> find_end_of_repetition([1, 1, 1, 1, 1, 1], 0, 1)
    5
    '''
    
    num_elem = len(int_list)
    
    for i in range(ind, num_elem):
        last_occur = i
        if int_list[i] != target_num:
            last_occur = i - 1
            break
    
    return last_occur


def compress(img_matrix):
    ''' (list<list<int>>) -> <list<list<str>>>
    Returns img_matrix with repeated integers in the form 'AxB'.
    
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    
    
    >>> compress([[5, 5, 5], [1, 2, 3], [4, 6, 5]])
    [['5x3'], ['1x1', '2x1', '3x1'], ['4x1', '6x1', '5x1']]
    
    >>> compress([[5, 5, 5, 6], [4, 4, 7, 8], [2, 2, 22, 4]])
    [['5x3', '6x1'], ['4x2', '7x1', '8x1'], ['2x2', '22x1', '4x1']]
    
    >>> compress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    Traceback (most recent call last):
    AssertionError: Input matrix must be in PGM image format.
    
    >>> compress([[5, 5, 5, 6], [4, 4, 7, 8], [2, 2, 2222, 4]])
    Traceback (most recent call last):
    AssertionError: Input matrix must be in PGM image format.
    '''
    
    if not(is_valid_image(img_matrix)):
        raise AssertionError('Input matrix must be in PGM image format.')
    
    num_row = len(img_matrix)
    num_col = len(img_matrix[0])
    comp_img_matrix = []
    
    for r in range(num_row):
        comp_row = []
        c = 0
        while c < num_col:
            target_num = img_matrix[r][c]
            last_occur = find_end_of_repetition(img_matrix[r], c, target_num)
            num_occur = last_occur - c + 1
            comp_row_elem = str(target_num) + 'x' + str(num_occur)
            comp_row.append(comp_row_elem)
            c += num_occur
        comp_img_matrix.append(comp_row)
            
    return comp_img_matrix


def decompress(comp_img_matrix):
    ''' (<list<list<str>>>) -> <list<list<int>>>
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    
    >>> image = [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> compressed_image = compress(image)
    >>> image2 = decompress(compressed_image)
    >>> image == image2
    True
    '''
    
    if not(is_valid_compressed_image(comp_img_matrix)):
        raise AssertionError('Input matrix must be in compressed PGM image format.')

    num_row = len(comp_img_matrix)
    img_matrix = []
    
    for r in range(num_row):
        num_col = len(comp_img_matrix[r])
        row = []
        for c in range(num_col):
            elem = comp_img_matrix[r][c].split('x')
            a = int(elem[0])
            b = int(elem[1])
            row_elem = [a] * b
            row += row_elem
        img_matrix.append(row)
        
    return img_matrix
    
    
def check_capital(elem):
    ''' (str) -> bool
    Returns True if all characters are capital letters
    and False if otherwise.
    
    >>> check_capital('ABX')
    True
    
    >>> check_capital('NGONRIFJDPSKC')
    True
    
    >>> check_capital('ABa')
    False
    
    >>> check_capital('D3')
    False
    
    >>> check_capital('fffff')
    False
    '''
    
    for letter in elem:
        if not(letter.isupper()):
            return False
    return True


def process_command(cmd):
    ''' (str) -> NoneType
    Uses the corresponding commands in cmd to call functions.
    'LOAD<x.pgm>' calls load_image(x.pgm), giving img_matrix.
    'INV' calls invert(img_matrix).
    'FH' calls flip_horizontal(img_matrix).
    'FV' calls flip_vertical(img_matrix).
    'CR<>y,x,h,w> calls crop(img_matrix, top_left_row, top_left_col, num_row, num_col).
    'CP' calls compress(img_matrix).
    'DC' calls decompress(img_matrix.)
    'SAVE<x.pgm>' calls save_image(x.pgm).
    AssertionError raised if unrecognized command is given
    
    >>> process_command('LOAD<comp.pgm> CP SAVE<comp.pgm.compressed>')
    >>> load_compressed_image('comp.pgm.compressed')
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> process_command('LOAD<comp.pgm> CR<3,3,4,9> SAVE<comp3.pgm>')
    >>> load_image('comp3.pgm')
    [[0, 0, 0, 0, 119, 0, 0, 0, 119], [0, 0, 0, 0, 119, 0, 0, 0, 119], [51, 51, 51, 0, 119, 119, 119, 119, 119], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> process_command('LOAD<mountain.pgm> CP SAVE<mountain.pgm.compressed>')
    >>> process_command('LOAD<mountain.pgm.compressed> DC SAVE<mountain2.pgm>')
    >>> image = load_image('mountain.pgm')
    >>> image2 = load_image('mountain2.pgm')
    >>> image == image2
    True
    
    >>> process_command('LOAD<dragon.pgm> FH FV I SAVE<dragonfhfvi.pgm>')
    Traceback (most recent call last):
    AssertionError: Input proper commands: LOAD, SAVE, INV, FH, FV, CR, CP, or DC.
    
    >>> process_command('LOAD<dragon.pgm> FH FV INV SAVE<dragonfhfvi.pgm>')
    >>> process_command('LOAD<dragonfhfvi.pgm> FH FV INV SAVE<dragonundo1.pgm>')
    >>> image = load_image('dragon.pgm')
    >>> image2 = load_image('dragonundo1.pgm')
    >>> image == image2
    True
    
    >>> process_command('LOAD<dragon.pgm> CR<50,3,20,30> CP SAVE<dragon.pgm.compressed>')
    >>> load_compressed_image('dragon.pgm.compressed')
    [['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x30'], ['255x29', '239x1'], ['255x27', '223x1', '95x1', '15x1'], ['255x25', '239x1', '95x1', '0x3'], ['255x24', '143x1', '15x1', '0x4'], ['255x22', '207x1', '47x1', '0x5', '14x1'], ['255x21', '159x1', '15x1', '0x4', '14x1', '95x1', '115x1']]
    
    >>> process_command('LOAD<comp.pgm> CP DC INd INV SAVE<comp2.pgm>')
    Traceback (most recent call last):
    AssertionError: Input proper commands: LOAD, SAVE, INV, FH, FV, CR, CP, or DC.
    
    >>> process_command('LOAD<comp.pgm> CP 1C INd INV SAVE<comp2.pgm>')
    Traceback (most recent call last):
    AssertionError: Input proper commands: LOAD, SAVE, INV, FH, FV, CR, CP, or DC.
    
    >>> process_command('LOAD<comp.pgm> @P 1C INd INV SAVE<comp2.pgm>')
    Traceback (most recent call last):
    AssertionError: Input proper commands: LOAD, SAVE, INV, FH, FV, CR, CP, or DC.
    
    >>> process_command('load<comp.pgm> cp save<comp.pgm.compressed>')
    Traceback (most recent call last):
    AssertionError: Input proper commands: LOAD, SAVE, INV, FH, FV, CR, CP, or DC.
    '''
    
    cmd_list = ['LOAD', 'SAVE', 'INV', 'FH', 'FV', 'CR', 'CP', 'DC']
    cmd = cmd.replace('<', ' <')
    cmd = cmd.replace(',', ' ')
    cmd = cmd.split(' ')
    i = 0
    
    while i < len(cmd) - 1:
        elem = cmd[i]
        is_upper = check_capital(elem)
        
        if not(is_upper) or elem not in cmd_list:
            raise AssertionError('Input proper commands: LOAD, SAVE, INV, FH, FV, CR, CP, or DC.')
        
        elif elem == 'LOAD':
            curr_file = cmd[i + 1][1:-1]
            img_matrix = load_image(curr_file)
            i += 1
        
        elif elem == 'INV':
            img_matrix = invert(img_matrix)
        
        elif elem == 'FH':
            img_matrix = flip_horizontal(img_matrix)
        
        elif elem == 'FV':
            img_matrix = flip_vertical(img_matrix)
        
        elif elem == 'CP':
            img_matrix = compress(img_matrix)
        
        elif elem == 'DC':
            img_matrix = decompress(img_matrix)
        
        elif elem == 'CR':
            top_left_row = int((cmd[i + 1])[1:])        # gets rid of '<' and converts to int
            top_left_col = int(cmd[i + 2])
            num_row = int(cmd[i + 3])
            num_col = int(cmd[i + 4][:-1])
            img_matrix = crop(img_matrix, top_left_row, top_left_col, num_row, num_col)
            i += 4
        
        elif elem == 'SAVE':
            curr_file = cmd[i + 1][1:-1]
            save_image(img_matrix, curr_file)
            
        i += 1
            

if __name__ == '__main__':
    doctest.testmod()