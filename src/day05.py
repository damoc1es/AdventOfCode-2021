# https://adventofcode.com/2021/day/5
input = "data/input05.txt"


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                print('.', end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()


def part1():
    with open(input, 'r') as file:
        size = 1000
        matrix = [[0] * size for _ in range(size)]

        for line in file:
            [P1, P2] = line.split(" -> ")
            [x1, y1] = [int(x) for x in P1.split(',')]
            [x2, y2] = [int(x) for x in P2.split(',')]

            if x1 == x2:
                if y1 > y2:
                    [y1, y2] = [y2, y1]

                for i in range(y1, y2 + 1):
                    matrix[x1][i] += 1
            elif y1 == y2:
                if x1 > x2:
                    [x1, x2] = [x2, x1]

                for i in range(x1, x2 + 1):
                    matrix[i][y1] += 1

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > 1:
                    count += 1

        return count


def part2():
    with open(input, 'r') as file:
        size = 1000
        matrix = [[0] * size for _ in range(size)]

        for line in file:
            [P1, P2] = line.split(" -> ")
            [x1, y1] = [int(x) for x in P1.split(',')]
            [x2, y2] = [int(x) for x in P2.split(',')]

            if x1 == x2:
                if y1 > y2:
                    [y1, y2] = [y2, y1]

                for i in range(y1, y2 + 1):
                    matrix[x1][i] += 1

            elif y1 == y2:
                if x1 > x2:
                    [x1, x2] = [x2, x1]

                for i in range(x1, x2 + 1):
                    matrix[i][y1] += 1

            elif abs(x2 - x1) == abs(y2 - y1):
                if x1 > x2:
                    [[x1, y1], [x2, y2]] = [[x2, y2], [x1, y1]]

                if y1 < y2:
                    for i in range(x2 - x1 + 1):
                        matrix[x1 + i][y1 + i] += 1
                else:
                    for i in range(x2 - x1 + 1):
                        matrix[x1 + i][y1 - i] += 1

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > 1:
                    count += 1

        return count


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
