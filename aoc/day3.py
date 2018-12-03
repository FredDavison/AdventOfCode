
from collections import namedtuple

from shared import read_input_lines, exec_cl_function


def part1(size=1000, file_='../input/day3.txt'):
    input_ = read_input_lines(file_, coerce=False)
    claims = [parse(line) for line in input_]
    fabric = [[0 for i in range(size)] for j in range(size)]
    overlaps = set()

    for i, claim in enumerate(claims):
        for other_claim in claims[i+1:]:
            if overlapping(claim, other_claim):
                overlaps.add(claim.id)
                overlaps.add(other_claim.id)
                # print(f'{claim.id} overlaps {other_claim.id}')
                update_fabric(fabric, claim, other_claim)
        if i % 50 == 0:
            print(total(fabric))

    for row in fabric:
        print(row[:min(len(row), 50)])
    print(f'total: {total(fabric)}')
    print('no overlaps: {}'.format({c.id for c in claims}.difference(overlaps)))


def part1example():
    part1(size=8, file_='../input/day3example.txt')


def part1test():
    part1(size=8, file_='../input/day3test.txt')


def parse(input_line):
    claim = namedtuple('claim', ['id', 'x', 'y'])
    _id, _, _coords, _dimensions = input_line.split()
    coords = [int(c) for c in _coords.replace(':', '').split(',')]
    dims = [int(d) for d in _dimensions.split('x')]
    x = [coords[0], coords[0] + dims[0] - 1]
    y = [coords[1], coords[1] + dims[1] - 1]
    return claim(_id, x, y)


def overlapping(area1, area2):
    x_overlap = (
        min(area2.x) <= min(area1.x) <= max(area2.x) or 
        min(area2.x) <= max(area1.x) <= max(area2.x) or
        min(area1.x) <= min(area2.x) <= max(area1.x) or 
        min(area1.x) <= max(area2.x) <= max(area1.x))
    y_overlap = (
        min(area2.y) <= min(area1.y) <= max(area2.y) or
        min(area2.y) <= max(area1.y) <= max(area2.y) or
        min(area1.y) <= max(area2.y) <= max(area1.y) or
        min(area1.y) <= max(area2.y) <= max(area1.y))

    return x_overlap and y_overlap


def update_fabric(fabric, area1, area2):
    start_x = max(area1.x[0], area2.x[0])
    end_x = min(area1.x[1], area2.x[1])
    start_y = max(area1.y[0], area2.y[0])
    end_y = min(area1.y[1], area2.y[1])

    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            fabric[y][x] = 1


def total(fabric):
    sum_ = 0
    for row in fabric:
        sum_ += sum(row)
    return sum_


if __name__ == '__main__':
    exec_cl_function()
