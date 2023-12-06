import numpy as numpy

from Timer import timer


def read_input(filename='input.txt'):
    with open(filename) as file:
        return file.readlines()


def parse_line(line):
    return [int(num) for num in line.split(':')[1].split()]


def good_hold_time(time, distance, hold_time):
    time_left = time - hold_time

    return time_left * hold_time > distance


def find_min_hold_time(time, distance):
    min_hold_time = 1
    max_hold_time = time - 1

    while min_hold_time < max_hold_time:
        mid_hold_time = (min_hold_time + max_hold_time) // 2
        if good_hold_time(time, distance, mid_hold_time):
            max_hold_time = mid_hold_time
        else:
            min_hold_time = mid_hold_time + 1

    return min_hold_time


def find_max_hold_time(time, distance):
    min_hold_time = 1
    max_hold_time = time - 1

    while min_hold_time < max_hold_time:
        mid_hold_time = (min_hold_time + max_hold_time + 1) // 2
        if good_hold_time(time, distance, mid_hold_time):
            min_hold_time = mid_hold_time
        else:
            max_hold_time = mid_hold_time - 1

    return max_hold_time


def simulate_race(race):
    min_hold_time = find_min_hold_time(race[0], race[1])
    max_hold_time = find_max_hold_time(race[0], race[1])

    return max_hold_time + 1 - min_hold_time


@timer
def part1(lines):
    times, distances = map(parse_line, lines[:2])
    numpy.prod(list(map(simulate_race, zip(times, distances))))
    print('Part 1:', numpy.prod(list(map(simulate_race, zip(times, distances)))))


@timer
def part2(lines):
    time = int(lines[0].split(':')[1].replace(' ', ''))
    distance = int(lines[1].split(':')[1].replace(' ', ''))

    print('Part 2:', simulate_race((time, distance)))


def main():
    lines = read_input()
    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
