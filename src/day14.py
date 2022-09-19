# https://adventofcode.com/2021/day/14
input = "data/input14.txt"


def polymerize(formula, combs, steps):
    pairs = {}
    for key in combs:
        pairs[key] = 0
    for i in range(len(formula) - 1):
        pairs[formula[i] + formula[i + 1]] += 1

    for _ in range(steps):
        new_pairs = {}
        for key in combs:
            new_pairs[key] = 0

        for pair, val in pairs.items():
            res1 = pair[0] + combs[pair]
            res2 = combs[pair] + pair[1]

            new_pairs[res1] += val
            new_pairs[res2] += val
        pairs = new_pairs

    values = {}
    for c in combs:
        values[c[0]] = 0

    for pair, val in pairs.items():
        values[pair[1]] += val

    values[formula[0]] += 1
    return values


def part1():
    with open(input, 'r') as file:
        formula = list(file.readline().strip())
        file.readline()
        combs = {}
        for line in file:
            pair, result = line.strip().split(" -> ")
            combs[pair] = result

        elements = polymerize(formula, combs, 10)

        return max(elements.values()) - min(elements.values())


def part2():
    with open(input, 'r') as file:
        formula = list(file.readline().strip())
        file.readline()
        combs = {}
        for line in file:
            pair, result = line.strip().split(" -> ")
            combs[pair] = result

        elements = polymerize(formula, combs, 40)

        return max(elements.values()) - min(elements.values())


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
