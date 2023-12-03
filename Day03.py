from collections import defaultdict

data = open('input.txt', 'r').read()
grid = []
for line in data.split('\n'):
    grid.append(line.strip())
n = len(grid)
m = len(grid[0])


def getNeighbors(i, j1, j2):
    neighbors = set()
    for j in range(j1, j2):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    neighbors.add((ni, nj))
    return neighbors


def isSymbol(char):
    return (not char.isdigit()) and (char != '.')


summe = 0
table = defaultdict(list)
for i in range(n):
    j = 0
    while j < m:
        if not grid[i][j].isdigit():
            j += 1
            continue
        j2 = j + 1
        while j2 < m and grid[i][j2].isdigit():
            j2 += 1
        if any(isSymbol(grid[nbri][nbrj]) for nbri, nbrj in getNeighbors(i, j, j2)):
            num = int(grid[i][j:j2])
            summe += num

            for ni, nj in getNeighbors(i, j, j2):
                if grid[ni][nj] == '*':
                    table[(ni, nj)].append(num)
        j = j2

print(summe)

gearRatioSum = 0
for v in table.values():
    if len(v) == 2:
        gearRatioSum += v[0] * v[1]
print(gearRatioSum)
