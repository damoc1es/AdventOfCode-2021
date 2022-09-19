# https://adventofcode.com/2021/day/13
input = "data/input13.txt"


def fold(points, axis, along):
    new_points = set()
    for (x, y) in points:
        if axis == 'y':
            if x > along:
                new_points.add((2 * along - x, y))
            else:
                new_points.add((x, y))
        else:
            if y > along:
                new_points.add((x, 2 * along - y))
            else:
                new_points.add((x, y))
    return new_points


def rendered_dots(points):
    max_x = max([x for (x, y) in points])
    max_y = max([y for (x, y) in points])
    Matrix = [['⬛'] * (max_y + 1) for _ in range(max_x + 1)]
    for (x, y) in points:
        Matrix[x][y] = '⬜'

    string = "\n"
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            string += Matrix[i][j]
        string += '\n'
    return string


def part1():
    with open(input, 'r') as file:
        points = set()
        folds = []
        for line in file:
            if line != '\n':
                if line.find("fold") == -1:
                    y, x = (int(i) for i in line.strip().split(','))
                    points.add((x, y))
                else:
                    folds = [line.strip().split('=')[0][-1], int(line.strip().split('=')[1])]
                    return len(fold(points, folds[0], folds[1]))


def part2():
    with open(input, 'r') as file:
        points = set()
        folds = []
        for line in file:
            if line != '\n':
                if line.find("fold") == -1:
                    y, x = (int(i) for i in line.strip().split(','))
                    points.add((x, y))
                else:
                    folds.append([line.strip().split('=')[0][-1], int(line.strip().split('=')[1])])
        for f in folds:
            points = fold(points, f[0], f[1])

        return rendered_dots(points)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
