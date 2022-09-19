# https://adventofcode.com/2021/day/2
input = "data/input02.txt"


def part1():
    with open(input, 'r') as file:
        horizontal = 0
        depth = 0

        for line in file:
            [x, c] = line.split()
            c = int(c)

            if x == "forward":
                horizontal += c
            elif x == "down":
                depth += c
            else:  # "up"
                depth -= c

        return horizontal * depth


def part2():
    with open(input, 'r') as file:
        aim = 0
        horizontal = 0
        depth = 0

        for line in file:
            [x, c] = line.split()
            c = int(c)

            if x == "forward":
                horizontal += c
                depth += aim * c
            elif x == "down":
                aim += c
            else:  # "up"
                aim -= c

        return horizontal * depth


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
