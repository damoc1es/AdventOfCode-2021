from collections import deque
from numpy import unique

# https://adventofcode.com/2021/day/19
input = "data/input19.txt"


def distance(p0, p1):  # actually using the square of the distance
    (x0, y0, z0) = p0
    (x1, y1, z1) = p1

    return (x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2


# https://www.euclideanspace.com/maths/algebra/matrix/transforms/examples/index.htm
# brain hurts
rotations = lambda x, y, z: [
    (x, y, z),
    (x, -z, y),
    (x, -y, -z),
    (x, z, -y),

    (-y, x, z),
    (z, x, y),
    (y, x, -z),
    (-z, x, -y),

    (-x, -y, z),
    (-x, -z, -y),
    (-x, y, -z),
    (-x, z, y),

    (y, -x, z),
    (z, -x, -y),
    (-y, -x, -z),
    (-z, -x, y),

    (-z, y, x),
    (y, z, x),
    (z, -y, x),
    (-y, -z, x),

    (-z, -y, -x),
    (-y, z, -x),
    (z, y, -x),
    (y, -z, -x)]


class Scanner:
    def __init__(self, id: int):
        self.id = id
        self.v = []
        self.rotation = -1
        self.original_v = []

    def reset(self):
        if self.original_v:
            self.v = self.original_v.copy()
            self.rotation = -1

    def rotate(self):
        if self.rotation == -1:
            self.original_v = self.v.copy()
        self.rotation += 1
        self.v = [rotations(x, y, z)[self.rotation] for (x, y, z) in self.original_v]

    def do_offset(self, offset):
        self.v = [(x + offset[0], y + offset[1], z + offset[2]) for (x, y, z) in self.v]

    def add(self, x, y, z):
        if (x, y, z) not in self.v:
            self.v.append((x, y, z))

    def __repr__(self):
        string = f"{self.id} : "
        for point in self.v:
            string += str(point) + " "
        return string

    def get(self) -> list:
        return self.v


cached_results = None


def literal_hell(scanners):
    known = scanners.popleft()  # assume scanner 0 as the correct scanner rotation
    max_manhattan = float("-inf")
    scanner_positions = [(0, 0, 0)]
    while scanners:
        found_overlap = False
        for scan in scanners:
            scan.reset()
            for _ in range(24):
                scan.rotate()
                differences = []

                known_lst = known.get()
                lst = scan.get()
                for p0 in known_lst:
                    for p1 in lst:
                        differences.append(distance(p0, p1))

                dst, counts = unique(differences, return_counts=True)

                if max(counts) >= 12:
                    found_overlap = True
                    dst_offset = -1
                    for i in range(len(counts)):
                        if counts[i] >= 12:
                            dst_offset = dst[i]
                            break

                    for p0 in known_lst:
                        for p1 in lst:
                            if distance(p0, p1) == dst_offset:
                                (x0, y0, z0) = p0
                                (x1, y1, z1) = p1

                                offset = (x0 - x1, y0 - y1, z0 - z1)
                                break
                    scanner_positions.append(offset)

                    scan.do_offset(offset)
                    scan_lst = scan.get()
                    for (x, y, z) in scan_lst:
                        known.add(x, y, z)

                    scanners.remove(scan)
                    break

            if found_overlap:
                break

    for i in range(len(scanner_positions)):
        for j in range(len(scanner_positions)):
            (x0, y0, z0) = scanner_positions[i]
            (x1, y1, z1) = scanner_positions[j]
            if max_manhattan < abs(x0 - x1) + abs(y0 - y1) + abs(z0 - z1):
                max_manhattan = abs(x0 - x1) + abs(y0 - y1) + abs(z0 - z1)

    global cached_results
    cached_results = len(known.get()), max_manhattan
    return len(known.get()), max_manhattan


def part1():
    if cached_results:
        return cached_results[0]
    with open(input, 'r') as file:
        scanners = deque()
        for line in file:
            if line.startswith("---"):
                scanners.append(Scanner(int(line.split()[2])))
                continue
            if line == '\n':
                continue

            (x, y, z) = [int(x) for x in line.strip().split(',')]
            scanners[-1].add(x, y, z)

        beacons, _ = literal_hell(scanners)

        return beacons


def part2():
    if cached_results is not None:
        return cached_results[1]
    with open(input, 'r') as file:
        scanners = deque()
        for line in file:
            if line.startswith("---"):
                scanners.append(Scanner(int(line.split()[2])))
                continue
            if line == '\n':
                continue

            (x, y, z) = [int(x) for x in line.strip().split(',')]
            scanners[-1].add(x, y, z)

        _, max_distance = literal_hell(scanners)

        return max_distance


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
