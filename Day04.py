data = open('input.txt', 'r')


def count_copies(scratch_cards):
    count = [1] * len(scratch_cards)
    for i, m in enumerate(scratch_cards):
        for j in range(i + 1, min(i + 1 + m, len(count))):
            count[j] += count[i]
    return sum(count)


cards = []
for line in data:
    card_data = line.split(': ')[1]
    left_nums = [int(num) for num in card_data.split(' | ')[0].split(' ') if num != '']
    right_nums = [int(num) for num in card_data.split(' | ')[1].split(' ') if num != '']
    winning_nums = [num for num in left_nums if num in right_nums]
    cards.append(len(winning_nums))

print(sum(2 ** (c - 1) for c in cards if c > 0))
print(count_copies(cards))
