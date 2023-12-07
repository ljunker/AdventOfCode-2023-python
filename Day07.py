from collections import Counter

from Timer import timer

lines = open('input.txt').read().strip().split('\n')


def hand_strength(hand, joker):
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1) if joker else chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    counter = Counter(hand)
    if joker:
        target = list(counter.keys())[0]
        for key in counter:
            if key != '1':
                if counter[key] > counter[target] or target == '1':
                    target = key
        assert target != '1' or list(counter.keys()) == ['1']
        if '1' in counter and target != '1':
            counter[target] += counter['1']
            del counter['1']
        assert '1' not in counter or list(counter.keys()) == ['1'], f'{counter} {hand}'

    match sorted(counter.values()):
        case [5]: return 7, hand
        case [1, 4]: return 6, hand
        case [2, 3]: return 5, hand
        case [1, 1, 3]: return 4, hand
        case [1, 2, 2]: return 3, hand
        case [1, 1, 1, 2]: return 2, hand
        case [1, 1, 1, 1, 1]: return 1, hand
        case _: assert False, f'{counter} {hand} {sorted(counter.values())}'


@timer
def part1():
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append((hand, bid))
    hands = sorted(hands, key=lambda hb: hand_strength(hb[0], False))
    total = 0
    for i, (hand, bid) in enumerate(hands):
        total += (i + 1) * int(bid)
    print(total)


@timer
def part2():
    hands_and_bids = []
    for line in lines:
        hand, bid = line.split()
        hands_and_bids.append((hand, bid))
    hands_and_bids = sorted(hands_and_bids, key=lambda hb: hand_strength(hb[0], True))
    total = 0
    for i, (hand, bid) in enumerate(hands_and_bids):
        total += (i + 1) * int(bid)
    print(total)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
