from itertools import product
from numpy import unique

# https://adventofcode.com/2021/day/21
input = "data/input21.txt"


def part1():
    with open(input, 'r') as file:
        pos1 = int(file.readline().split(": ")[1])
        pos2 = int(file.readline().split(": ")[1])
        score = [0, 0]
        rolled = 0
        i = 1
        position = [pos1, pos2]
        while max(score) < 1000:
            i += 1
            player = i % 2
            roll = (rolled % 100) + 1
            rolled += 1
            roll += (rolled % 100) + 1
            rolled += 1
            roll += (rolled % 100) + 1
            rolled += 1

            position[player] = (position[player] - 1 + roll) % 10 + 1

            score[player] += position[player]
        return rolled * min(score)


quantum_possible = []
quantum_cached = {}


def quantum_play(i, position, score, roll):
    player = i % 2

    cache = (player, position[0], position[1], score[0], score[1], roll)
    global quantum_cached
    if cache in quantum_cached:
        return quantum_cached[cache]

    position[player] = (position[player] - 1 + roll) % 10 + 1
    score[player] += position[player]

    if max(score) >= 21:
        if score[0] >= 21:
            return (1, 0)
        return (0, 1)

    global quantum_possible
    wins = (0, 0)
    for next_roll, universes in quantum_possible.items():
        win0, win1 = quantum_play(i + 1, position.copy(), score.copy(), next_roll)
        wins = (wins[0] + win0 * universes, wins[1] + win1 * universes)

    quantum_cached[cache] = wins
    return wins


def part2():
    with open(input, 'r') as file:
        pos1 = int(file.readline().split(": ")[1])
        pos2 = int(file.readline().split(": ")[1])
        arr = [1, 2, 3]
        global quantum_possible
        uniq, counts = unique([sum(comb) for comb in product(arr, arr, arr)], return_counts=True)
        quantum_possible = dict(zip(uniq, counts))

        position = [pos1, pos2]

        wins = (0, 0)
        scores = [0, 0]
        for roll, universes in quantum_possible.items():
            win0, win1 = quantum_play(0, position.copy(), scores.copy(), roll)
            wins = (wins[0] + win0 * universes, wins[1] + win1 * universes)
        return max(wins)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
