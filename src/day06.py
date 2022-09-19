# https://adventofcode.com/2021/day/6
input = "data/input06.txt"


def part1():
    with open(input, 'r') as file:
        lanternfish = [0 for _ in range(9)]
        for c in file.readline().split(','):
            lanternfish[int(c)] += 1

        for _ in range(80):
            stage0 = lanternfish[0]
            for i in range(8):
                lanternfish[i] = lanternfish[i + 1]
            lanternfish[6] += stage0
            lanternfish[8] = stage0

        return sum(lanternfish)


def part2():
    with open(input, 'r') as file:
        lanternfish = [0 for _ in range(9)]
        for c in file.readline().split(','):
            lanternfish[int(c)] += 1

        for _ in range(256):
            stage0 = lanternfish[0]
            for i in range(8):
                lanternfish[i] = lanternfish[i + 1]
            lanternfish[6] += stage0
            lanternfish[8] = stage0

        return sum(lanternfish)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
