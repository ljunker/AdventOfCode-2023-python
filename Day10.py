from Timer import timer

with open("input.txt", "r") as f:
    lines = f.readlines()

pipe_types = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
}

directions = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

field = [[c for c in line.strip()] for line in lines]

encountered = dict()


@timer
def part1(start):
    queue = [(start, 0)]
    while len(queue) > 0:
        current, distance = queue.pop(0)
        if current in encountered:
            continue
        encountered[current] = distance
        i, j = current
        available_directions = pipe_types[field[i][j]]
        for direction in available_directions:
            di, dj, opposite = directions[direction]
            new = (i + di, j + dj)
            if i + di < 0 or i + di >= len(field):
                continue
            if j + dj < 0 or j + dj >= len(field[i + di]):
                continue
            target = field[i + di][j + dj]
            if target not in pipe_types:
                continue
            target_directions = pipe_types[target]
            if opposite in target_directions:
                queue.append((new, distance + 1))
    max_distance = max(encountered.values())
    print(max_distance)


def get_piece_type(i, j):
    reachable_directions = []
    for direction in directions:
        di, dj, opposite = directions[direction]
        if i + di < 0 or i + di >= len(field):
            continue
        if j + dj < 0 or j + dj >= len(field[i + di]):
            continue
        if (i + di, j + dj) not in encountered:
            continue
        target = field[i + di][j + dj]
        if target not in pipe_types:
            continue
        target_directions = pipe_types[target]
        if opposite not in target_directions:
            continue
        reachable_directions.append(direction)
    for piece_type in pipe_types:
        if len(reachable_directions) == len(pipe_types[piece_type]):
            if all([direction in pipe_types[piece_type] for direction in reachable_directions]):
                return piece_type
    return None


@timer
def part2(start):
    field[start[0]][start[1]] = get_piece_type(start[0], start[1])
    for i in range(len(field)):
        norths = 0
        for j in range(len(field[i])):
            place = field[i][j]
            if (i, j) in encountered:
                pipe_directions = pipe_types[place]
                if "n" in pipe_directions:
                    norths += 1
                continue
            if norths % 2 == 0:
                field[i][j] = "O"
            else:
                field[i][j] = "I"
    # print field line for line
    for line in field:
        print("".join(line))
    count = "\n".join(["".join(line) for line in field]).count("I")
    print(count)


def main():
    start = (0, 0)
    for i in range(len(field)):
        for j in range(len(field[i])):
            place = field[i][j]
            if place == 'S':
                start = (i, j)
    part1(start)
    part2(start)


if __name__ == '__main__':
    main()
