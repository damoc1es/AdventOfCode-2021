# https://adventofcode.com/2021/day/17
input = "data/input17.txt"


def step(pos, velocity):
    x, y = pos
    x_vel, y_vel = velocity
    x = x + x_vel
    y = y + y_vel
    if x_vel < 0:
        x_vel += 1
    elif x_vel > 0:
        x_vel -= 1
    y_vel -= 1
    return (x, y), (x_vel, y_vel)


def in_box(pos, box_x, box_y):
    return box_x[0] <= pos[0] <= box_x[1] and box_y[0] <= pos[1] <= box_y[1]


def cant_hit(pos, box_x, box_y):
    return pos[0] > box_x[1] or pos[1] < box_y[0]


iterations = 300


def part1():
    with open(input, 'r') as file:
        string = file.readline().strip()
        (x, y) = [w.split('=')[-1].split('..') for w in string.split(', ')]

        box_x = [int(x0) for x0 in x]
        box_y = [int(y0) for y0 in y]

        max_y = float('-inf')
        for i in range(iterations):
            for j in range(-iterations, iterations):
                pos = (0, 0)
                velocity = (i, j)
                measured_y = 0
                while not cant_hit(pos, box_x, box_y):
                    pos, velocity = step(pos, velocity)
                    if measured_y < pos[1]:
                        measured_y = pos[1]
                    if in_box(pos, box_x, box_y):
                        if max_y < measured_y:
                            max_y = measured_y
                        break
        return max_y


def part2():
    with open(input, 'r') as file:
        string = file.readline().strip()
        (x, y) = [w.split('=')[-1].split('..') for w in string.split(', ')]

        box_x = [int(x0) for x0 in x]
        box_y = [int(y0) for y0 in y]

        solutions = set()
        for i in range(iterations):
            for j in range(-iterations, iterations):
                pos = (0, 0)
                velocity = (i, j)
                while not cant_hit(pos, box_x, box_y):
                    pos, velocity = step(pos, velocity)
                    if in_box(pos, box_x, box_y):
                        solutions.add((i, j))
                        break
        return len(solutions)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
