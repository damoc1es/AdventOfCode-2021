# https://adventofcode.com/2021/day/16
input = "data/input16.txt"


def decode_packet(packet):
    version = int(packet[:3], 2)
    packet = packet[3:]

    type_id = int(packet[:3], 2)
    packet = packet[3:]

    if type_id == 4:
        groups = []
        group_b = '1'
        while group_b != '0':
            group_b = packet[:1]
            groups.append(packet[1:5])
            packet = packet[5:]

        value = ""
        for group in groups:
            value += group

        return int(value, 2), packet, version
    else:  # operators
        length_type_id = packet[:1]
        packet = packet[1:]
        values = []
        sum_version = version

        if length_type_id == '0':
            subpackets_size = int(packet[:15], 2)

            packet = packet[15:]
            ops = packet[:subpackets_size]

            while ops != '' and '1' in ops:
                value, ops, v = decode_packet(ops)
                values.append(value)
                sum_version += v
            packet = packet[subpackets_size:]
        else:  # '1'
            number_subpackets = int(packet[:11], 2)
            packet = packet[11:]

            for _ in range(number_subpackets):
                value, packet, v = decode_packet(packet)
                values.append(value)
                sum_version += v

        if type_id == 0:
            return sum(values), packet, sum_version
        if type_id == 1:
            p = 1
            for val in values:
                p *= val
            return p, packet, sum_version
        if type_id == 2:
            return min(values), packet, sum_version
        if type_id == 3:
            return max(values), packet, sum_version
        if type_id == 5:
            b = 1 if values[0] > values[1] else 0
            return b, packet, sum_version
        if type_id == 6:
            b = 1 if values[0] < values[1] else 0
            return b, packet, sum_version
        if type_id == 7:
            b = 1 if values[0] == values[1] else 0
            return b, packet, sum_version


def part1():
    with open(input, 'r') as file:
        binary = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
        }
        transmission = file.readline().strip()
        code = ''.join([binary[c] for c in transmission])
        _, _, version_sum = decode_packet(code)
        return version_sum


def part2():
    with open(input, 'r') as file:
        binary = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
        }
        transmission = file.readline().strip()
        code = ''.join([binary[c] for c in transmission])

        return decode_packet(code)[0]


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
