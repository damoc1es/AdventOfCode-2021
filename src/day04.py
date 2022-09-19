from copy import deepcopy

# https://adventofcode.com/2021/day/4
input = "data/input04.txt"


def is_bingo(table) -> bool:
    for i in range(5):
        bingo = True
        for j in range(5):
            if table[i][j] != '-':
                bingo = False
                break
        if bingo:
            return True

    for i in range(5):
        bingo = True
        for j in range(5):
            if table[j][i] != '-':
                bingo = False
                break
        if bingo:
            return True
    return False


def try_mark_bingo(table, number: str) -> bool:
    found = False
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == number:
                table[i][j] = '-'
                found = True

    return found


def part1():
    with open(input, 'r') as file:
        numbers = file.readline().strip().split(',')
        currently_winning = []
        winning_draw = float('inf')

        table = []
        for line in file:
            if line.strip():
                table.append(line.strip().split())
                if len(table) == 5:
                    for index, draw in enumerate(numbers):
                        if try_mark_bingo(table, draw) and is_bingo(table):
                            if index < winning_draw:
                                currently_winning = deepcopy(table)
                                winning_draw = index
                            break
                    table.clear()

        sum_unmarked = 0
        for i in range(5):
            for j in range(5):
                if currently_winning[i][j] != '-':
                    sum_unmarked += int(currently_winning[i][j])

        return sum_unmarked * int(numbers[winning_draw])


def part2():
    with open(input, 'r') as file:
        numbers = file.readline().strip().split(',')
        currently_winning = []
        winning_draw = float('-inf')

        table = []
        for line in file:
            if line.strip():
                table.append(line.strip().split())
                if len(table) == 5:
                    for index, draw in enumerate(numbers):
                        if try_mark_bingo(table, draw) and is_bingo(table):
                            if index > winning_draw:
                                currently_winning = deepcopy(table)
                                winning_draw = index
                            break
                    table.clear()

        sum_unmarked = 0
        for i in range(5):
            for j in range(5):
                if currently_winning[i][j] != '-':
                    sum_unmarked += int(currently_winning[i][j])

        return sum_unmarked * int(numbers[winning_draw])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
