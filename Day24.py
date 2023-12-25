import sys

import numpy as np

from util import *

sys.setrecursionlimit(100000)
lines = []

for line in get_input_from_file("input.txt"):
    line = line.strip()
    lines.append(
        tuple(
            tuple([float(a) for a in s.split(", ")]) for s in line.split(" @ ")
        )
    )


def part1():
    answer = 0

    test_area = (200000000000000, 400000000000000)

    for itx in range(len(lines)):
        for jtx in range(itx + 1, len(lines)):
            a = lines[itx]
            b = lines[jtx]

            (apx, apy, _), (avx, avy, _) = a
            (bpx, bpy, _), (bvx, bvy, _) = b

            try:
                y = (bpx - (bvx / bvy * bpy) + (avx / avy * apy) - apx) / (
                        avx / avy - bvx / bvy
                )
                x = ((y - apy) / avy) * avx + apx

                if (
                        test_area[0] <= x <= test_area[1]
                        and test_area[0] <= y <= test_area[1]
                ):
                    if (
                            np.sign(x - apx) == np.sign(avx)
                            and np.sign(y - apy) == np.sign(avy)
                            and np.sign(x - bpx) == np.sign(bvx)
                            and np.sign(y - bpy) == np.sign(bvy)
                    ):
                        answer += 1

            except:
                pass

    print(f"Part 1: {answer}")


def part2():
    import z3
    answer = 0

    solver = z3.Solver()
    x, y, z, vx, vy, vz = [z3.Int(var) for var in ["x", "y", "z", "vx", "vy", "vz"]]

    for itx in range(4):
        (cpx, cpy, cpz), (cvx, cvy, cvz) = lines[itx]

        t = z3.Int(f"t{itx}")
        solver.add(t >= 0)
        solver.add(x + vx * t == cpx + cvx * t)
        solver.add(y + vy * t == cpy + cvy * t)
        solver.add(z + vz * t == cpz + cvz * t)

    if solver.check() == z3.sat:
        model = solver.model()
        (x, y, z) = (model.eval(x), model.eval(y), model.eval(z))
        answer = x.as_long() + y.as_long() + z.as_long()
    print(f"Part 2: {answer}")


part1()
part2()
