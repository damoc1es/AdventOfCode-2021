from numpy import median

# https://adventofcode.com/2021/day/7
input = "data/input07.txt"


def part1():
    with open(input, 'r') as file:
        crabs = [int(x) for x in file.readline().split(',')]
        median_crab = round(median(crabs))

        least_fuel = sum([abs(crab - median_crab) for crab in crabs])
        return least_fuel


def part2():
    def triangle_number(n):
        return n * (n + 1) // 2

    with open(input, 'r') as file:
        crabs = [int(x) for x in file.readline().split(',')]
        freq = [0] * (max(crabs) + 1)
        for crab in crabs:
            freq[crab] += 1

        least_fuel = float("inf")

        for i in range(len(freq)):
            fuel = 0
            for j in range(len(freq)):
                if freq[j]:
                    fuel += (triangle_number(abs(i - j)) * freq[j])

            if fuel < least_fuel:
                least_fuel = fuel

        return least_fuel


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
