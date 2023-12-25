import sys
from collections import deque

from Timer import timer
from util import make_grid, get_input_from_file, write_input_to_file

write_input_to_file(2023, 23, "input.txt")

DATA = get_input_from_file("input.txt")
grid, rows, cols = make_grid(DATA)

sys.setrecursionlimit(10000000)


def solve(slippy_slopey):
    vertices = set()
    for r in range(rows):
        for c in range(cols):
            nbr = 0
            for ch, dr, dc in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] != '#':
                    nbr += 1
            if nbr > 2 and grid[r][c] != '#':
                vertices.add((r, c))

    start = (0, 1)
    end = (rows - 1, cols - 2)
    vertices.add(start)
    vertices.add(end)

    edges = {}
    for (rv, cv) in vertices:
        edges[(rv, cv)] = []
        Q = deque([(rv, cv, 0)])
        seen = set()
        while Q:
            r, c, d = Q.popleft()
            if (r, c) in seen:
                continue
            seen.add((r, c))
            if (r, c) in vertices and (r, c) != (rv, cv):
                edges[(rv, cv)].append(((r, c), d))
                continue
            for ch, dr, dc in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] != '#':
                    if slippy_slopey and grid[r][c] in ['<', '>', '^', 'v'] and grid[r][c] != ch:
                        continue
                    Q.append((r + dr, c + dc, d + 1))

    count = 0
    ans = 0
    seen = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(v, d):
        nonlocal count
        nonlocal ans
        count += 1
        r, c = v
        if seen[r][c]:
            return
        seen[r][c] = True
        if r == rows - 1:
            ans = max(ans, d)
        for (y, yd) in edges[v]:
            dfs(y, d + yd)
        seen[r][c] = False

    dfs(start, 0)
    return ans


@timer
def part1():
    print(solve(True))


@timer
def part2():
    print(solve(False))


part1()
part2()
