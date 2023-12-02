from Timer import timer

data = open('input.txt', 'r').read()


@timer
def part1():
    limits = {'red': 12, 'green': 13, 'blue': 14}
    count = 0

    lines = data.split('\n')
    for line in lines:
        valid = True
        game_id = int(line.split(':')[0].split(' ')[1])
        sets = line.split(':')[1]

        for set in sets.split(';'):
            for cubes in set.strip().split(', '):
                for color in limits.keys():
                    if cubes.split(' ')[1] == color and int(cubes.split(' ')[0]) > limits[color]:
                        valid = False
        if valid:
            count += game_id
    print(count)


@timer
def part2():
    summe = 0
    for line in data.split('\n'):
        red, green, blue = [], [], []

        for sets in line.split(':')[1].split(';'):
            for cubes in sets.strip().split(', '):
                if cubes.split(' ')[1] == 'red':
                    red.append(int(cubes.split(' ')[0]))
                if cubes.split(' ')[1] == 'green':
                    green.append(int(cubes.split(' ')[0]))
                if cubes.split(' ')[1] == 'blue':
                    blue.append(int(cubes.split(' ')[0]))
        summe += max(red) * max(green) * max(blue)
    print(summe)


part1()
part2()
print("Done")
