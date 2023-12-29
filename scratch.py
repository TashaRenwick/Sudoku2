import numpy as np
import random

bank = [1,2,3,4,5,6,7,8,9]

def print_puzzle(puzzle):
    '''
    This prints a puzzle "prettily"
    :param puzzle:
    :return:
    '''

    for row_index, row in enumerate(puzzle):

        if row_index % 3 == 0:
            print('-' * 37, end='\n')

        print('| ', end='')
        for index, entry in enumerate(row):
            if index == 0:
                print(entry, end='', sep='')
            elif index % 3 == 0:
                print(' | ', entry, end='', sep='')
            else:
                print('  ', entry, end='')

        print(' | ')


    print('-'*37)

    return None

def available_numbers(line):
    '''
    This compares the numbers present in a list (could be row, line or box) and returns a list of valid numbers
    :param line:
    :return:
    '''
    available = set(bank) - set(line)
    return list(available)

def generate_puzzle():
    '''
    Returns:
    1) A puzzle with random entries 1-9
    2) A "working puzzle" made of
    :return:
    '''

    # Puzzle
    ls = [random.randint(1, 9) for x in range(81)]
    puzzle = np.array(ls)

    # Working
    ls = [bank for x in range(81)]
    working = np.array(ls)

    return puzzle.reshape((9, 9)), working.reshape((9,9))

working = np.array(bank)

print(working*21)

bank = list(range(1,10))

ls = [random.randint(1,9) for x in range(81)]

array = np.array(ls)
puzzle = array.reshape((9,9))

print_puzzle(puzzle)



