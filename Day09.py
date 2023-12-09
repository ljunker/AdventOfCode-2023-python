from Timer import timer


@timer
def main():
    summe = 0
    firsts = []
    with open('input.txt') as f:
        for row in [[int(i) for i in line.split()] for line in f.readlines()]:
            first = []
            while row:
                summe += row[-1]
                first.append(row[0])
                row = [j - i for i, j in zip(row, row[1:])]
            firsts.append(first)

    print('part1: ', summe)
    summe = [(-n if i % 2 else n) for row in firsts for i, n in enumerate(row)]
    print('part2: ', sum(summe))


if __name__ == '__main__':
    main()
