lines = open("input.txt").readlines()
grid = [list(line.strip()) for line in lines]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

rows = len(grid)
cols = len(grid[0])
print(rows, cols)

q = set()
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            q.add((i, j))

goal = 26501365

a = []
for step in range(1, 1000000):
    new_q = set()
    for i, j in q:
        for k in range(4):
            new_i = i + dx[k]
            new_j = j + dy[k]
            if grid[new_i % rows][new_j % cols] != "#":
                new_q.add((new_i, new_j))
    q = new_q
    if step == 64:
        print("part1: ", len(q))
    if step % rows == goal % rows:
        a.append((step, len(q)))
        print(step, len(q), step // rows)
    if len(a) == 3:
        break


# newton polynom interpolation over a
x = [a[i][0] for i in range(3)]
y = [a[i][1] for i in range(3)]
coeff0 = y[0]
coeff1_a = (y[1] - y[0]) / (x[1] - x[0])
coeff1_b = (y[2] - y[1]) / (x[2] - x[1])
coeff2 = (coeff1_b - coeff1_a) / (x[2] - x[0])
interpolated = coeff0 + coeff1_a * (goal - x[0]) + coeff2 * (goal - x[0]) * (goal - x[1])


print("part2: ", interpolated)
