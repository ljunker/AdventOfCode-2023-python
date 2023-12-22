from Timer import timer

inp = open("input.txt").read().strip()


class Brick:
    def __init__(self, line: str):
        c0 = [int(x) for x in line.split("~")[0].split(",")]
        c1 = [int(x) for x in line.split("~")[1].split(",")]
        self.xrange = list(range(c0[0], c1[0] + 1))
        self.yrange = list(range(c0[1], c1[1] + 1))
        self.h0 = c0[2]
        self.h1 = c1[2]
        self.supporting = []
        self.resting_on = []
        self.falling = False

    def minheight(self):
        return min(self.h0, self.h1)

    def maxheight(self):
        return max(self.h0, self.h1)

    def overlaps(self, b):
        o_x = False
        o_y = False
        for x in self.xrange:
            if x in b.xrange:
                o_x = True
                break
        if not o_x:
            return False
        for y in self.yrange:
            if y in b.yrange:
                o_y = True
                break
        return o_y

    def recursive_fall(self):
        self.falling = True
        s = 0
        for x in self.supporting:
            if len([y for y in x.resting_on if not y.falling]) == 0:
                s += 1
                s += x.recursive_fall()
        return s


def drop(bricks):
    for n, brick in enumerate(bricks):
        for x in range(n - 1, -1, -1):
            rest_height = brick.resting_on[0].maxheight() if brick.resting_on else 1
            if brick.overlaps(bricks[x]):
                new_height = bricks[x].maxheight()
                if not brick.resting_on or new_height > rest_height:
                    for y in brick.resting_on:
                        y.supporting.remove(brick)
                    brick.resting_on = [bricks[x]]
                    bricks[x].supporting.append(brick)
                elif new_height == rest_height:
                    brick.resting_on.append(bricks[x])
                    bricks[x].supporting.append(brick)
        height_diff = brick.minheight() - (brick.resting_on[0].maxheight() + 1) if brick.resting_on else brick.minheight() - 1
        brick.h0 -= height_diff
        brick.h1 -= height_diff


@timer
def part1():
    total = 0
    bricks = [Brick(line) for line in inp.splitlines()]
    bricks = sorted(bricks, key=lambda b: b.minheight())
    drop(bricks)
    for brick in bricks:
        if all([len(x.resting_on) > 1 for x in brick.supporting]):
            total += 1
    print(total)
    return bricks


@timer
def part2():
    total = 0
    bricks = [Brick(line) for line in inp.splitlines()]
    bricks = sorted(bricks, key=lambda b: b.minheight())
    drop(bricks)
    for brick in bricks:
        for x in bricks:
            x.falling = False
        total += brick.recursive_fall()
    print(total)
    return bricks


part1()
part2()
