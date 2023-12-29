import numpy as np
import random


def print_puzzle(puzzle):

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
    available = set(bank) - set(line)
    return list(available)



bank = list(range(1,10))

ls = [random.randint(1,9) for x in range(81)]

array = np.array(ls)
puzzle = array.reshape((9,9))

print_puzzle(puzzle)



