# https://adventofcode.com/2021/day/10
input = "data/input10.txt"

opposite = {'(': ')', '[': ']', '{': '}', '<': '>'}

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']


def part1():
    with open(input, 'r') as file:
        points = {')': 3, ']': 57, '}': 1197, '>': 25137}

        score = 0
        for line in file:
            chunk = list(line.strip())

            stack = []
            for char in chunk:
                if char in opening:
                    stack.append(char)
                elif char in closing:
                    if opposite[stack[-1]] != char:
                        score += points[char]
                        break
                    else:
                        stack.pop()
        return score


def part2():
    with open(input, 'r') as file:
        points = {')': 1, ']': 2, '}': 3, '>': 4}

        scores = []
        for line in file:
            chunk = list(line.strip())
            corrupted = False

            stack = []
            for char in chunk:
                if char in opening:
                    stack.append(char)
                elif char in closing:
                    if opposite[stack[-1]] != char:
                        score += points[char]
                        corrupted = True
                        break
                    else:
                        stack.pop()

            if not corrupted and len(stack):
                score = 0
                while len(stack):
                    score *= 5
                    score += points[opposite[stack[-1]]]
                    stack.pop()
                scores.append(score)

        scores.sort()
        return scores[len(scores) // 2]


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
