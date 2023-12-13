from Timer import timer


def find_reflection(pattern, skip_line=None):
    for row in range(len(pattern) - 1):
        line = (row, None)
        if line == skip_line:
            continue

        a = pattern[: row + 1][::-1]
        b = pattern[row + 1:]

        found = True
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                found = False
                break

        if found:
            return line, 100 * len(a)

    for col in range(len(pattern[0]) - 1):
        line = (None, col)
        if line == skip_line:
            continue

        a = [pattern[i][: col + 1][::-1] for i in range(len(pattern))]
        b = [pattern[i][col + 1:] for i in range(len(pattern))]

        found = True
        for i in range(min(len(a[0]), len(b[0]))):
            if [c[i] for c in a] != [c[i] for c in b]:
                found = False
                break

        if found:
            return line, len(a[0])


def find_reflection_fix_smudge(pattern):
    reflection, _ = find_reflection(pattern)

    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            pattern[i][j] = "#" if pattern[i][j] == "." else "."
            new_reflection = find_reflection(pattern, reflection)
            if new_reflection is not None and new_reflection[0] != reflection:
                return new_reflection[1]
            pattern[i][j] = "#" if pattern[i][j] == "." else "."


def main():
    lines = open("input.txt").read().strip()
    patterns = lines.split("\n\n")
    part1(patterns)

    part2(patterns)


@timer
def part2(patterns):
    part2_sum = 0
    for pattern in patterns:
        pattern = [[c for c in line] for line in pattern.split("\n")]
        part2_sum += find_reflection_fix_smudge(pattern)
    print(part2_sum)


@timer
def part1(patterns):
    part1_sum = 0
    for pattern in patterns:
        pattern = [[c for c in line] for line in pattern.split("\n")]
        _, amount = find_reflection(pattern)
        part1_sum += amount
    print(part1_sum)


if __name__ == "__main__":
    main()
