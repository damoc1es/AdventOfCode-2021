# https://adventofcode.com/2021/day/3
input = "data/input03.txt"


def part1():
    with open(input, 'r') as file:
        gamma = []
        size = 12
        bit0 = [0] * size
        line_count = 0

        for line in file:
            binary = line.strip()
            line_count += 1

            for i in range(len(binary)):
                if binary[i] == '0':
                    bit0[i] += 1

        for i in range(size):
            gamma.append('0' if bit0[i] > line_count / 2 else '1')

        epsilon = int(''.join(['1' if gamma[i] == '0' else '0' for i in range(size)]), 2)
        gamma = int(''.join(gamma), 2)

        return gamma * epsilon


def part2():
    # bar == '0' ? keeps least common bit
    # bar == '1' ? keeps most common bit
    def keep_x_common_bit(lst: list, index: int, bar: str) -> str:
        if len(lst) == 1:
            return lst[0]

        bit1 = 0

        for line in lst:
            if line[index] == '1':
                bit1 += 1

        kept_bit = bar
        if bit1 < len(lst) / 2:
            kept_bit = '0' if bar == '1' else '1'

        return keep_x_common_bit([line for line in lst if line[index] == kept_bit], index + 1, bar)

    with open(input, 'r') as file:
        lines = [line.strip() for line in file]

    oxygen = int(keep_x_common_bit(lines.copy(), 0, '1'), 2)
    co2 = int(keep_x_common_bit(lines.copy(), 0, '0'), 2)
    return oxygen * co2


def part2_non_recursive():
    with open(input, 'r') as file:
        lines_copy = [line.strip() for line in file]

    lines = lines_copy.copy()
    index = 0
    while len(lines) > 1:
        bit0 = bit1 = 0

        for line in lines:
            if line[index] == '0':
                bit0 += 1
            else:
                bit1 += 1

        kept_bit = '1'
        if bit1 < bit0:
            kept_bit = '0'

        lines = [line for line in lines if line[index] == kept_bit]
        index += 1
    oxygen = int(lines[0], 2)

    lines = lines_copy.copy()
    index = 0
    while len(lines) > 1:
        bit0 = bit1 = 0

        for line in lines:
            if line[index] == '0':
                bit0 += 1
            else:
                bit1 += 1

        kept_bit = '0'
        if bit1 < bit0:
            kept_bit = '1'

        lines = [line for line in lines if line[index] == kept_bit]
        index += 1
    co2 = int(lines[0], 2)

    return oxygen * co2


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
