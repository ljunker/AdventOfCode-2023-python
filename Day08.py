from math import gcd

from Timer import timer


def solve(instructions, maps, current):
    count = 0
    while True:
        i = instructions[count % len(instructions)]
        if current[2] == 'Z' and count != 0:
            break
        count += 1
        if i == 'L':
            i = 0
        else:
            i = 1

        current = maps[current][i]
    return count, current


@timer
def part1(instructions, maps):
    count, current = solve(instructions, maps, 'AAA')
    assert current == 'ZZZ'
    print(count)


@timer
def part2(instructions, maps):
    starts = [k for k in maps.keys() if k[2] == 'A']
    counts = []
    for current in starts:
        count, at1 = solve(instructions, maps, current)
        counts.append(count)
    lcm = 1
    for count in counts:
        lcm = lcm * count // gcd(lcm, count)
    print(lcm)


def get_input():
    lines = open('input.txt').read().strip().split('\n')
    instructions = lines[0]
    maps = {}
    for line in lines[2:]:
        a, b = line.split(' = ')
        maps[a] = (b[1:4], b[6:9])
    return instructions, maps


def main():
    instructions, maps = get_input()
    part1(instructions, maps)
    part2(instructions, maps)


if __name__ == '__main__':
    main()
