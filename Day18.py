from functools import reduce

from Timer import timer

data = open('input.txt', 'r').readlines()
move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def calc_area(trench, perimeter):
    area = reduce(lambda current, points: current + (points[0][0] * points[1][1] - points[1][0] * points[0][1]),
                  [(i, j) for i, j in zip(trench, trench[1:])],
                  0)
    interior_area = abs(area) // 2 + perimeter // 2 + 1
    return interior_area


@timer
def part1():
    x, y, trench = 0, 0, []
    perimeter = 0
    for row in data:
        d, m, _ = row.split()
        m = int(m)
        dx, dy = move[d]
        x, y = x + dx * m, y + dy * m
        perimeter += m
        trench.append((x, y))

    interior_area = calc_area(trench, perimeter)
    print('Part 1:', interior_area)


@timer
def part2():
    x, y, trench = 0, 0, []
    perimeter = 0
    for row in data:
        _, _, c = row.split()
        c = c[1:-1]
        d, m = dirs[c[-1]], int(c[1:-1], 16)
        dx, dy = move[d]
        x, y = x + dx * m, y + dy * m
        perimeter += m
        trench.append((x, y))

    interior_area = calc_area(trench, perimeter)
    print('Part 2:', interior_area)


part1()
part2()
