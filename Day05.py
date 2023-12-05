from typing import List, Optional, Tuple

from Timer import timer


class RangedMap(object):
    def __init__(self):
        self.sources = []
        self.destinations = []
        self.lengths = []

    def __getitem__(self, key: int):
        for i, s in enumerate(self.sources):
            if s <= key < s + self.lengths[i]:
                return self.destinations[i] + key - s
        return key

    def mapSingleRange(self, start: int, length: int, r_source_start: int, r_dest_start: int, r_length: int) -> \
            Optional[Tuple[int, int, int]]:
        end = start + length
        r_end = r_source_start + r_length
        # rate mal wie lang der part gedauert hat
        if r_source_start >= end or start >= r_end:
            return None
        if r_source_start <= start < r_end <= end:
            return start, start - r_source_start + r_dest_start, r_end - start
        if r_end >= end > r_source_start >= start:
            return r_source_start, r_dest_start, end - r_source_start
        if end >= r_end and start <= r_source_start:
            return r_source_start, r_dest_start, r_length
        if r_end >= end and r_source_start <= start:
            return start, r_dest_start + start - r_source_start, length
        raise Exception("AAAAAAAAAAAAA")

    def mapRange(self, start: int, length: int) -> List[List[int]]:
        dest_range = []
        source_range = []
        for i, source in enumerate(self.sources):
            v = self.mapSingleRange(start, length, source, self.destinations[i], self.lengths[i])
            if not v:
                continue
            s, d, l = v
            dest_range.append((d, l))
            source_range.append((s, l))

        source_range.sort()
        c_start = start
        for (s, l) in source_range:
            if c_start < s:
                dest_range.append((c_start, s - c_start))
            c_start = s + l
        if c_start < start + length:
            dest_range.append((c_start, start + length - c_start))
        return sorted(dest_range)

    def add_range(self, source: int, destination: int, length: int):
        self.sources.append(source)
        self.destinations.append(destination)
        self.lengths.append(length)

    def __repr__(self):
        return f"RangedMap({self.sources}, {self.destinations}, {self.lengths})"


def parse_seeds(i_line):
    return [int(num) for num in i_line[len("seeds: "):].split()]


@timer
def part1(i_seeds, i_maps):
    min_loc = float('inf')
    for seed in i_seeds:
        min_loc = min(min_loc, get_location(seed, i_maps))
    print(min_loc)


@timer
def part2(i_seeds, i_maps):
    next_seeds = []
    i_seeds = [(i_seeds[i], i_seeds[i + 1]) for i in range(0, len(i_seeds), 2)]
    print(str(sum(num for _, num in i_seeds)) + " seeds")
    for _, ranged_map in i_maps.items():
        next_seeds = []
        for start, length in i_seeds:
            next_seeds.extend(ranged_map.mapRange(start, length))
        i_seeds = next_seeds
    next_seeds.sort()
    print(next_seeds[0][0])


def parse_map(line):
    mapping, _ = line.split()
    source, _, dest = mapping.split("-")
    return source, dest


def parse_range(line):
    source, dest, length = line.strip().split()
    return int(source), int(dest), int(length)


def get_location(seed, maps):
    s = seed
    for _, ranged_map in maps.items():
        # print(seed, dest, s, source, map[s])
        s = ranged_map[s]
    return s


maps = {}
with open("input.txt") as file:
    seeds = parse_seeds(file.readline())

    line = file.readline()
    r_map = None
    while line:
        line = line.strip()
        if not line:
            pass
        elif "map:" in line:
            source_name, dest_name = parse_map(line)
            r_map = RangedMap()
            maps[(source_name, dest_name)] = r_map
        else:
            d, s, r = parse_range(line)
            r_map.add_range(s, d, r)
        line = file.readline()
part1(seeds, maps)
part2(seeds, maps)
