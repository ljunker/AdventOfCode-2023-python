from Timer import timer


def count_copies(scratch_cards):
    count = [1] * len(scratch_cards)
    for i, m in enumerate(scratch_cards):
        for j in range(i + 1, min(i + 1 + m, len(count))):
            count[j] += count[i]
    return sum(count)


def get_cards():
    cards = []
    for line in open('input.txt'):
        card_data = line.split(': ')[1]
        left_nums = [int(num) for num in card_data.split(' | ')[0].split()]
        right_nums = [int(num) for num in card_data.split(' | ')[1].split()]
        winning_nums = [num for num in left_nums if num in right_nums]
        cards.append(len(winning_nums))
    return cards


@timer
def part1():
    cards = get_cards()
    print(sum(2 ** (c - 1) for c in cards if c > 0))


@timer
def part2():
    cards = get_cards()
    print(count_copies(cards))


part1()
part2()
