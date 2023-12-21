from copy import deepcopy

from Timer import timer


def parse_lines(data):
    instructions = {}
    ratings = []
    is_ratings = False
    for line in data:
        line = line.strip()
        if len(line) == 0:
            is_ratings = True
            continue
        if not is_ratings:
            l = line.split('{')
            name = l[0]
            parts = [part.split(':') for part in l[1][:-1].split(',')]
            parts = [
                [(part[0][0], part[0][1], int(part[0][2:])), part[1]]
                if len(part) == 2
                else part
                for part in parts
            ]
            instructions[name] = parts
        else:
            l = [a.split('=') for a in line[1:-1].split(',')]
            l = dict((k, int(v)) for [k, v] in l)
            ratings.append(l)
    return instructions, ratings


@timer
def part1(instructions, ratings):
    answer = 0

    for rating in ratings:
        curr = handle_rating(instructions, rating)

        if curr == "A":
            answer += sum(rating.values())

    print(f"Part 1: {answer}")


def handle_rating(instructions, rating):
    curr = "in"
    while curr not in ["A", "R"]:
        rules = instructions[curr]
        curr = apply_rule(curr, rating, rules)
    return curr


def apply_rule(curr, rating, rules):
    for r in rules:
        if len(r) == 1:
            curr = r[0]
            break

        (var, condition, value) = r[0]
        result = r[1]

        if condition == ">":
            if rating[var] > value:
                curr = result
                break
        else:
            if rating[var] < value:
                curr = result
                break
    return curr


def range_size(ranges):
    result = 1
    for r in ranges.values():
        result *= r[1] - r[0] + 1
    return result


def solve(instructions, ranges, curr):
    parts = instructions[curr]
    val = 0

    for part in parts:
        if len(part) == 1:
            if part[0] == "A":
                val += range_size(ranges)
            elif part[0] != "R":
                val += solve(instructions, ranges, part[0])
        else:
            (var, cond, amount) = part[0]
            destination = part[1]

            range_var = ranges[var]

            if cond == ">":
                if range_var[1] > amount:
                    range_copy = deepcopy(ranges)
                    range_copy[var] = (max(range_var[0], amount + 1), range_var[1])

                    if destination == "A":
                        val += range_size(range_copy)
                    elif destination != "R":
                        val += solve(instructions, range_copy, destination)

                ranges[var] = (range_var[0], amount)
            else:
                if range_var[0] < amount:
                    range_copy = deepcopy(ranges)
                    range_copy[var] = (range_var[0], min(range_var[1], amount - 1))

                    if destination == "A":
                        val += range_size(range_copy)
                    elif destination != "R":
                        val += solve(instructions, range_copy, destination)

                ranges[var] = (amount, range_var[1])

    return val


@timer
def part2(instructions):
    ranges = {}
    for val in "xmas":
        ranges[val] = [1, 4000]
    answer = solve(instructions, ranges, "in")

    print(f"Part 2: {answer}")


def main():
    data = open('input.txt', 'r').readlines()
    (instructions, ratings) = parse_lines(data)
    part1(instructions, ratings)
    part2(instructions)


if __name__ == '__main__':
    main()
