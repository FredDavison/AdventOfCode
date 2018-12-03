
from shared import read_input_lines, exec_cl_function
from collections import Counter


def letter_repeats(strings, recurrences=(2, 3)):
    counts = {r: [] for r in recurrences}
    for string in strings:
        for n in recurrences:
            counts[n].append(contains_letter_repeated_n(n, string))
    return counts


def contains_letter_repeated_n(n, string):
    '''True if string contains a letter repeated n times'''
    counter = Counter(string)
    return bool([k for k, v in counter.items() if v == n])


def part1():
    strings = read_input_lines('../input/day2.txt', coerce=False)
    repeats = letter_repeats(strings)
    print(sum(repeats[2]) * sum(repeats[3]))


def part2():
    strings = read_input_lines('../input/day2.txt', coerce=False)
    total = len(strings)
    for i, string in enumerate(strings):
        others = strings[:i] + strings[i+1:]
        print(f'{i} / {total}', end='\r')
        for i, other in enumerate(others):
            one_difference = differs_by_one(string, other)
            if one_difference:
                print(f'string1: {string}')
                print(f'string2: {other}')
                print(f'difference: {str(set(string).difference(other))}')
                print(f'common string: {one_difference}')
                return


def differs_by_one(string1, string2):
    n_differing = 0
    common = ''
    for i, (l1, l2) in enumerate(zip(string1, string2)):
        if l1 == l2:
            common += l1
        elif n_differing == 0:
            n_differing += 1
        else:
            return
    return common


if __name__ == '__main__':
    exec_cl_function()
