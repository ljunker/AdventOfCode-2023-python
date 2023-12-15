from functools import reduce

hash_char = lambda i, c: (i + ord(c)) * 17 % 256
make_hash = lambda s: reduce(hash_char, s, 0)

puzzle_input = open("input.txt").read().strip().split(",")
print("part1: ", sum(map(make_hash, puzzle_input)))

boxes = [dict() for _ in range(256)]
for instruction in puzzle_input:
    match instruction.strip('-').split('='):
        case [l, f]:
            boxes[make_hash(l)][l] = int(f)
        case [l]:
            boxes[make_hash(l)].pop(l, 0)

print("part2: ", sum(i * j * f for i, b in enumerate(boxes, 1) for j, f in enumerate(b.values(), 1)))
