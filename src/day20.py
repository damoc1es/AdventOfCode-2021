import numpy as np

# https://adventofcode.com/2021/day/20
input = "data/input20.txt"


def matrix_to_int(matrix):
    string = ""
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            string += str(matrix[i, j])

    return int(string, 2)


def enhance(algorithm, image, step):
    if algorithm[0] != 0 and step % 2 == 1:
        image = np.pad(image, 2, constant_values=1)
        result = np.ones_like(image)
    else:
        image = np.pad(image, 2, constant_values=0)
        result = np.zeros_like(image)

    n, m = image.shape
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            result[i, j] = algorithm[matrix_to_int(image[i - 1:i + 2, j - 1:j + 2])]

    return result[1:-1, 1:-1]


def part1():
    with open(input, 'r') as file:
        algo = [0 if c == '.' else 1 for c in file.readline().strip()]
        file.readline()
        matrix = []
        for line in file:
            matrix.append([0 if c == '.' else 1 for c in line.strip()])

        matrix = np.matrix(matrix)

        for i in range(2):
            matrix = enhance(algo, matrix, i)

        return matrix.sum()


def part2():
    with open(input, 'r') as file:
        algo = [0 if c == '.' else 1 for c in file.readline().strip()]
        file.readline()
        matrix = []
        for line in file:
            matrix.append([0 if c == '.' else 1 for c in line.strip()])

        matrix = np.matrix(matrix)

        for i in range(50):
            matrix = enhance(algo, matrix, i)

        return matrix.sum()


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
