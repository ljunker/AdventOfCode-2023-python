from collections import deque
from math import lcm

from Timer import timer

lines = open("input.txt").readlines()

adj = {}
conjs = {}
ffs = {}
rx_conj = ""

for line in lines:
    module, dests = line.strip().split(" -> ")
    dests = dests.split(", ")
    t = module[0]
    if module == "broadcaster":
        adj["broadcaster"] = dests
    else:
        label = module[1:]
        adj[label] = dests

    if "rx" in dests:
        rx_conj = label

    if t == "&":
        conjs[label] = {}

    if t == "%":
        ffs[label] = False

for label, dests in adj.items():
    for dest in dests:
        if dest in conjs:
            conjs[dest][label] = 0

low_pulses = 0
high_pulses = 0
presses = 0
rx_conj_presses = {}


def press():
    global low_pulses, high_pulses, presses
    presses += 1

    low_pulses += 1 + len(adj["broadcaster"])
    queue = deque()
    for dest in adj["broadcaster"]:
        queue.append((0, "broadcaster", dest))

    while queue:
        pulse, src, label = queue.popleft()

        if label == "rx":
            continue

        # conjunction
        to_send = 0
        if label in conjs:
            conjs[label][src] = pulse
            if any(n == 0 for n in conjs[label].values()):
                to_send = 1

        # flip-flop
        if label in ffs:
            if pulse == 1:
                continue
            ffs[label] = not ffs[label]
            if ffs[label]:
                to_send = 1

        # increment low or high pulses
        if to_send == 1:
            high_pulses += len(adj[label])
        else:
            low_pulses += len(adj[label])

        # send pulse to destination modules
        for dest in adj[label]:
            queue.append((to_send, label, dest))

        # check if any of the inputs connected to the conjunction
        # connected to "rx" are one and record the number of presses
        for label, val in conjs[rx_conj].items():
            if val == 1 and label not in rx_conj_presses:
                rx_conj_presses[label] = presses


@timer
def part1():
    for _ in range(1000):
        press()

    print(low_pulses * high_pulses)


@timer
def part2():
    while len(rx_conj_presses) < 4:
        press()

    print(lcm(*rx_conj_presses.values()))


part1()
part2()
