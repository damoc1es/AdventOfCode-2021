# https://adventofcode.com/2021/day/12
input = "data/input12.txt"


def visit(lst, linked, visited, semaphore):
    x = lst[-1]
    counter = 0

    for cave in linked[x]:
        if not (cave.lower() == cave and visited[cave]) or (visited[cave] == 1 and semaphore):
            lst.append(cave)
            visited[cave] += 1
            if cave == 'end':
                counter += 1
            else:
                if (cave.lower() == cave and visited[cave] == 2 and semaphore) or not semaphore:
                    counter += visit(lst, linked, visited, False)
                else:
                    counter += visit(lst, linked, visited, True)
            lst.pop()
            visited[cave] -= 1

    return counter


def part1():
    linked = {}
    visited = {}

    with open(input, 'r') as file:
        for line in file:
            [x, y] = line.strip().split('-')
            if x not in linked: linked[x] = []
            if y not in linked: linked[y] = []
            if y != 'start':
                linked[x].append(y)
            if x != 'start':
                linked[y].append(x)
            visited[x] = visited[y] = 0

        return visit(['start'], linked, visited, False)


def part2():
    linked = {}
    visited = {}

    with open(input, 'r') as file:
        for line in file:
            [x, y] = line.strip().split('-')
            if x not in linked: linked[x] = []
            if y not in linked: linked[y] = []
            if y != 'start':
                linked[x].append(y)
            if x != 'start':
                linked[y].append(x)
            visited[x] = visited[y] = 0

        return visit(['start'], linked, visited, True)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
