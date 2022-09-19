# https://adventofcode.com/2021/day/22
input = "data/input22.txt"


class Cuboid:
    def __init__(self, x, y, z, state=True):
        self.state = state
        self.x = (x[0], x[1])
        self.y = (y[0], y[1])
        self.z = (z[0], z[1])

    def corners(self):
        lst = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    lst.append((self.x[i], self.y[j], self.z[k]))
        return lst

    def intersects(self, other) -> bool:
        if self.x[0] < other.x[1] and self.x[1] > other.x[0]:
            if self.y[0] < other.y[1] and self.y[1] > other.y[0]:
                if self.z[0] < other.z[1] and self.z[1] > other.z[0]:
                    return True
        return False

    def contains(self, point):
        x, y, z = point
        if self.x[0] <= x < self.x[1]:
            if self.y[0] <= y < self.y[1]:
                if self.z[0] <= z < self.z[1]:
                    return True
        return False

    def entirely_in(self, other) -> bool:
        if other.x[0] <= self.x[0] and other.x[1] >= self.x[1]:
            if other.y[0] <= self.y[0] and other.y[1] >= self.y[1]:
                if other.z[0] <= self.z[0] and other.z[1] >= self.z[1]:
                    return True
        return False

    def minus(self, other):
        if not self.intersects(other):
            return [self]
        if self.entirely_in(other):
            return []

        x_axis = sorted([self.x[0], self.x[1], other.x[0], other.x[1]])
        y_axis = sorted([self.y[0], self.y[1], other.y[0], other.y[1]])
        z_axis = sorted([self.z[0], self.z[1], other.z[0], other.z[1]])

        sol = []

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    cube = Cuboid((x_axis[i], x_axis[i + 1]), (y_axis[j], y_axis[j + 1]), (z_axis[k], z_axis[k + 1]))
                    if cube.entirely_in(self) and not cube.intersects(other):
                        sol.append(cube)
        return sol

    def volume(self):
        if self.x[0] < self.x[1] and self.y[0] < self.y[1] and self.z[0] < self.z[1]:
            return (self.x[1] - self.x[0]) * (self.y[1] - self.y[0]) * (self.z[1] - self.z[0])
        return 0

    def __str__(self):
        return f"[({self.x[0]},{self.x[1]}), ({self.y[0]},{self.y[1]}), ({self.z[0]},{self.z[1]})]"


def part1():
    with open(input, 'r') as file:
        instructions = []
        for line in file:
            state, pos = line.strip().split()
            if state == "on":
                state = True
            else:
                state = False

            x, y, z = [w.split('=')[-1].split("..") for w in pos.split(',')]
            x = [int(c) for c in x]
            y = [int(c) for c in y]
            z = [int(c) for c in z]
            instructions.append((state, (x, y, z)))

        cubes = set()
        for instruction in instructions:
            x, y, z = instruction[1]

            for i in range(max(x[0], -50), min(x[1] + 1, 51)):
                for j in range(max(y[0], -50), min(y[1] + 1, 51)):
                    for k in range(max(z[0], -50), min(z[1] + 1, 51)):
                        if instruction[0]:
                            cubes.add((i, j, k))
                        elif (i, j, k) in cubes:
                            cubes.remove((i, j, k))

        return len(cubes)


def part2():
    with open(input, 'r') as file:
        lst = []
        for line in file:
            state, pos = line.strip().split()
            if state == "on":
                state = True
            else:
                state = False

            x, y, z = [w.split('=')[-1].split("..") for w in pos.split(',')]
            x = [int(c) for c in x]
            y = [int(c) for c in y]
            z = [int(c) for c in z]
            lst.append(Cuboid((x[0], x[1] + 1), (y[0], y[1] + 1), (z[0], z[1] + 1), state))

        on_cubes = []

        for cube in lst:

            new_list = []
            for another_cube in on_cubes:
                new_list.extend(another_cube.minus(cube))
            on_cubes = new_list

            if cube.state:
                on_cubes.append(cube)

        return sum([cube.volume() for cube in on_cubes])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
