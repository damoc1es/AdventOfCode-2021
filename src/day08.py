# https://adventofcode.com/2021/day/8
input = "data/input08.txt"


def part1():
    with open(input, 'r') as file:
        count = 0
        for line in file:
            for number in line.split('|')[1].split():
                if len(number) in [2, 3, 4, 7]:
                    count += 1

        return count


def part2():
    with open(input, 'r') as file:
        output_sum = 0
        for line in file:
            [input_numbers, output_numbers] = [x.split() for x in line.split('|')]
            sets = {}

            sets[1] = [s for s in input_numbers if len(s) == 2][0]
            sets[4] = [s for s in input_numbers if len(s) == 4][0]
            sets[7] = [s for s in input_numbers if len(s) == 3][0]
            sets[8] = [s for s in input_numbers if len(s) == 7][0]
            for x in sets:
                input_numbers.remove(sets[x])
                sets[x] = set(sets[x])

            real = {}
            for char in sets[7]:
                if char not in sets[1]:
                    real['a'] = char

            six_sticks = [nr for nr in input_numbers if len(nr) == 6]
            for nr in six_sticks:
                input_numbers.remove(nr)

            for nr in six_sticks:
                if real['a'] in nr and len(set(nr) - sets[4] - set(real['a'])) == 1:
                    real['g'] = min(set(nr) - sets[4] - set(real['a']))
                    sets[9] = set(nr)
                    six_sticks.remove(nr)
                    break

            real['e'] = min(sets[8] - sets[4] - set(real['a'] + real['g']))

            for nr in six_sticks:
                if len(set(nr) - (sets[7] | set(real['e'] + real['g']))) == 1:
                    sets[0] = set(nr)
                    six_sticks.remove(nr)
                    break

            sets[6] = set(six_sticks[0])

            for nr in input_numbers:
                if set(nr) == sets[6] - set(real['e']):
                    sets[5] = set(nr)
                    input_numbers.remove(nr)
                    break

            for nr in input_numbers:
                if len(set(nr) - (sets[7] | set(real['g']))) == 1:
                    sets[3] = set(nr)
                    input_numbers.remove(nr)
                    break

            sets[2] = set(input_numbers[0])  # the only remaining digit to decipher

            deciphered = 0
            p = 1000
            for number in output_numbers:
                for i in sets:
                    if sets[i] == set(number):
                        deciphered += p * i
                        p //= 10

            output_sum += deciphered
        return output_sum


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
