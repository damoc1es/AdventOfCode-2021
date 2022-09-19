# https://adventofcode.com/2021/day/11
input = "data/input11.txt"


def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


di = [0, 0, 0, -1, -1, -1, 1, 1, 1]
dj = [0, -1, 1, 0, -1, 1, 0, -1, 1]


def is_ok(matrix, i, j):
    if i < 0 or j < 0:
        return False
    if i >= len(matrix) or j >= len(matrix[0]):
        return False
    return True


def flash(matrix, i, j, flash_matrix):
    flash_matrix[i][j] = True
    for d in range(9):
        [new_i, new_j] = [i + di[d], j + dj[d]]
        if is_ok(matrix, new_i, new_j):
            matrix[new_i][new_j] += 1
            if matrix[new_i][new_j] > 9 and not flash_matrix[new_i][new_j]:
                flash(matrix, new_i, new_j, flash_matrix)


def step(matrix):
    flash_matrix = [[False] * len(matrix) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] += 1

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > 9 and not flash_matrix[i][j]:
                flash(matrix, i, j, flash_matrix)

    counter = 0
    for i in range(len(flash_matrix)):
        for j in range(len(flash_matrix[i])):
            if flash_matrix[i][j]:
                counter += 1
                matrix[i][j] = 0

    return counter


def part1():
    with open(input, 'r') as file:
        matrix = []
        for line in file:
            matrix.append([int(x) for x in list(line.strip())])
        counter = 0
        for _ in range(100):
            counter += step(matrix)
        return counter


def part2():
    with open(input, 'r') as file:
        matrix = []
        for line in file:
            matrix.append([int(x) for x in list(line.strip())])
        i = 1
        while step(matrix) != 100:
            i += 1
        return i


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
