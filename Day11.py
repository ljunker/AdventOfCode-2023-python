Point = complex


def get_dist(a, b):
    return int(abs(a.imag - b.imag) + abs(a.real - b.real))


def solve(points, empty, part1=True):
    factor = 1 if part1 else 1000000 - 1
    grid = []
    for point in points:
        modifier = Point(
            sum(a < point.real for a in empty[0]),
            sum(a < point.imag for a in empty[1])
        ) * factor
        grid.append(point + modifier)

    total = 0
    for i in range(len(grid) - 1):
        for j in range(i + 1, len(grid)):
            total += get_dist(grid[i], grid[j])
    return total


def main():
    lines = open('input.txt').read().strip().split('\n')

    points = []
    lim = len(lines)
    empty = [set(range(lim)), set(range(lim))]

    for y, l in enumerate(lines):
        for x, v in enumerate(l):
            if v == '#':
                points.append(Point(x, y))
                empty[0] -= {x}
                empty[1] -= {y}

    print("part1: ", solve(points, empty, True))
    print("part2: ", solve(points, empty, False))


if __name__ == '__main__':
    main()
