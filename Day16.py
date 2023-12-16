import sys
from collections import defaultdict

from Timer import timer

sys.setrecursionlimit(1_000_000)

puzzle_input = open('input.txt').read()
grid = [list(line) for line in puzzle_input.splitlines()]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_names = ['R', 'L', 'D', 'U']
mirrors = {
    '.': {'R': ['R'], 'L': ['L'], 'D': ['D'], 'U': ['U']},
    '-': {'R': ['R'], 'L': ['L'], 'D': ['L', 'R'], 'U': ['L', 'R']},
    '|': {'R': ['D', 'U'], 'L': ['D', 'U'], 'D': ['D'], 'U': ['U']},
    '/': {'R': ['U'], 'L': ['D'], 'D': ['L'], 'U': ['R']},
    '\\': {'R': ['D'], 'L': ['U'], 'D': ['R'], 'U': ['L']},
}


def count_from(start):
    energized = defaultdict(int)

    def energize(x, y, direction):
        if (x, y, direction) in energized:
            return
        energized[(x, y, direction)] += 1
        mirror = grid[x][y]
        for direction in mirrors[mirror][direction]:
            next_dir = dirs[dir_names.index(direction)]
            next_x = x + next_dir[0]
            next_y = y + next_dir[1]
            if next_x in range(len(grid)) and next_y in range(len(grid[0])):
                energize(next_x, next_y, direction)

    energize(start[0], start[1], start[2])
    return len(set([(x, y) for x, y, _ in energized]))


@timer
def part1():
    print(count_from((0, 0, 'R')))


@timer
def part2():
    configurations = []
    for x in range(len(grid)):
        configurations.append((x, 0, 'R'))
        configurations.append((x, len(grid[0]) - 1, 'L'))
    for y in range(len(grid[0])):
        configurations.append((0, y, 'D'))
        configurations.append((0, len(grid) - 1, 'U'))
    print(max(count_from(config) for config in configurations))


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
