from Timer import timer

cache = {}


def get_ways(row, nums):
    if (row, tuple(nums)) in cache:
        return cache[(row, tuple(nums))]

    if len(nums) == 0:
        return 1 if "#" not in row else 0

    size = nums[0]
    total = 0

    for i in range(len(row)):
        if (
                i + size <= len(row) and
                all(c != "." for c in row[i: i + size]) and
                (i == 0 or row[i - 1] != "#") and
                (i + size == len(row) or row[i + size] != "#")
        ):
            total += get_ways(row[i + size + 1:], nums[1:])

        if row[i] == "#":
            break

    cache[(row, tuple(nums))] = total
    return total


@timer
def get_total(lines, times=1):
    total = 0

    for line in lines:
        row, nums = line.split()
        row = "?".join([row] * times)
        nums = [int(n) for n in nums.split(",")] * times
        total += get_ways(row, nums)
    return total


def main():
    total = get_total(open('input.txt').read().strip().split('\n'))
    print("part1: ", total)
    total = get_total(open('input.txt').read().strip().split('\n'), 5)
    print("part2: ", total)


if __name__ == '__main__':
    main()
