from itertools import cycle

from shared import read_input_lines, exec_cl_function

INPUT = '../input/day1.txt'


def first_duplicate():
    total = 0
    seen = set()
    for freq in cycle(read_input_lines(INPUT, convert_to=int)):
        total += freq
        if total in seen:
            return total, len(seen)
        seen.add(total)


def part1():
    print(sum(read_input_lines(INPUT, convert_to=int)))


def part2():
    print('first duplicate result {} after {:,d} calculations'.format(
        *first_duplicate()))


if __name__ == '__main__':
    exec_cl_function()
