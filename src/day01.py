# https://adventofcode.com/2021/day/1
input = "data/input01.txt"


def part1():
    with open(input, 'r') as file:
        c = 0
        x = int(file.readline())

        for line in file:
            y = int(line)

            if x < y:
                c += 1

            x = y

        return c


def part2():
    with open("data/input01.txt", 'r') as file:
        c = 0
        sum_ = 0
        [x, y, z] = [int(file.readline()) for _ in range(3)]

        for line in file:
            w = int(line)
            if x + y + z < y + z + w:
                c += 1

            x = y
            y = z
            z = w

        return c


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
