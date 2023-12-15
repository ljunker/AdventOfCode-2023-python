def tilt_turn(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                ny = y
                grid[ny][x] = '.'
                while ny >= 0 and grid[ny][x] == '.':
                    ny -= 1
                grid[ny + 1][x] = 'O'
    return list(map(list, zip(*grid[::-1])))


def cycle(grid):
    for i in range(4):
        grid = tilt_turn(grid)
    return grid


def calc_load(grid):
    ans = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                ans += len(grid) - y
    return ans


def main():
    puzzle_input = open('input.txt').read().strip()
    grid = [list(l) for l in puzzle_input.splitlines()]
    tilt_turn(grid)
    part1 = calc_load(grid)
    print("part1: ", part1)

    seen = {}
    fast_forward = False

    turn = 0
    target = 1000000000
    while turn < target:
        grid = cycle(grid)
        turn += 1
        grid_hash = str(grid)

        if not fast_forward and grid_hash in seen:
            period = turn - seen[grid_hash]
            turn += ((target - turn) // period) * period
            fast_forward = True

        seen[grid_hash] = turn
    print("part2: ", calc_load(grid))


if __name__ == '__main__':
    main()
