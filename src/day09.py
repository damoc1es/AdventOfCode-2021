# https://adventofcode.com/2021/day/9
input = "data/input09.txt"


def is_ok(matrix, i, j):
    if i < 0 or j < 0:
        return False
    if i >= len(matrix) or j >= len(matrix[0]):
        return False
    return True


di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
areas = []


def fill(matrix, i, j):
    matrix[i][j] = -1 * len(areas)
    areas[-1] += 1
    for d in range(4):
        [new_i, new_j] = [i + di[d], j + dj[d]]

        if is_ok(matrix, new_i, new_j) and matrix[new_i][new_j] != 9 and matrix[new_i][new_j] >= 0:
            fill(matrix, new_i, new_j)


def part1():
    with open(input, 'r') as file:
        matrix = []
        for line in file:
            matrix.append([int(x) for x in list(line.strip())])

        sum_low_points = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                low = True
                for d in range(4):
                    if is_ok(matrix, i + di[d], j + dj[d]) and matrix[i][j] >= matrix[i + di[d]][j + dj[d]]:
                        low = False
                        break
                if low:
                    sum_low_points += matrix[i][j] + 1
        return sum_low_points


def part2():
    with open(input, 'r') as file:
        matrix = []
        for line in file:
            matrix.append([int(x) for x in list(line.strip())])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 9 and matrix[i][j] >= 0:
                    areas.append(0)
                    fill(matrix, i, j)

        areas.sort(reverse=True)
        return areas[0] * areas[1] * areas[2]


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
