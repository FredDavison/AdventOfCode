import sys
from itertools import cycle


def read_input(coerce=True):
    with open('input.txt') as f:
        freqs = f.readlines()
    if coerce:
        return [int(f) for f in freqs]
    return freqs



def first_duplicate():
    total = 0
    seen = set()
    for freq in cycle(read_input()):
        total += freq
        if total in seen:
            return total, len(seen)
        seen.add(total)


def part1():
    print(sum(read_input()))


def part2():
    print('first duplicate result {} after {:,d} calculations'.format(
        *first_duplicate()))


if __name__ == '__main__':
    getattr(sys.modules[__name__], sys.argv[1])()
