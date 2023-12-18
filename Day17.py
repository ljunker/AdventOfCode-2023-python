import heapq

from Timer import timer

lines = open('input.txt').readlines()
grid = [[int(c) for c in row.strip()] for row in lines]
rows = len(grid)
columns = len(grid[0])
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


@timer
def solve(part2):
    q = [(0, 0, 0, -1, -1)]
    visited = {}
    while q:
        dist, y, x, _dir, dir_count = heapq.heappop(q)
        if (y, x, _dir, dir_count) in visited:
            continue
        visited[(y, x, _dir, dir_count)] = dist
        for i, (dy, dx) in enumerate(dirs):
            new_y = y + dy
            new_x = x + dx
            new_dir = i
            new_dir_count = (1 if new_dir != _dir else dir_count + 1)

            isnt_reverse = ((new_dir + 2) % 4 != _dir)

            isvalid_part1 = (new_dir_count <= 3)
            isvalid_part2 = (new_dir_count <= 10 and (new_dir == _dir or dir_count >= 4 or dir_count == -1))
            isvalid = (isvalid_part2 if part2 else isvalid_part1) and isnt_reverse

            if 0 <= new_y < rows and 0 <= new_x < columns and isvalid:
                cost = int(grid[new_y][new_x])
                heapq.heappush(q, (dist + cost, new_y, new_x, new_dir, new_dir_count))

    ans = 1e9
    for (y, x, _dir, dir_count), v in visited.items():
        if y == rows - 1 and x == columns - 1:
            ans = min(ans, v)
    return ans


print(solve(False))
print(solve(True))
