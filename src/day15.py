from queue import PriorityQueue

# https://adventofcode.com/2021/day/15
input = "data/input15.txt"


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print()


def is_ok(matrix, i, j):
    if i < 0 or j < 0:
        return False
    if i >= len(matrix) or j >= len(matrix[i]):
        return False
    return True


def dijkstra(matrix):
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    dist = [[float("inf")] * len(matrix[0]) for _ in range(len(matrix))]
    dist[0][0] = 0

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    in_queue = set()
    in_queue.add((0, 0))

    while pq.qsize():
        _, node = pq.get()
        in_queue.remove(node)
        i, j = node

        for d in range(4):
            new_i, new_j = i + di[d], j + dj[d]
            if is_ok(matrix, new_i, new_j):
                if dist[i][j] + matrix[new_i][new_j] < dist[new_i][new_j]:
                    dist[new_i][new_j] = dist[i][j] + matrix[new_i][new_j]

                    if (new_i, new_j) not in in_queue:
                        pq.put((dist[new_i][new_j], (new_i, new_j)))
                        in_queue.add((new_i, new_j))

    return dist[-1][-1]


def part1():
    with open(input, 'r') as file:
        matrix = []
        for line in file:
            matrix.append([int(x) for x in list(line.strip())])

        return dijkstra(matrix)


def part2():
    def increment(n):
        return (n + 1) % 10 if n < 9 else 1

    with open(input, 'r') as file:
        matrix = []
        for line in file:
            lst = [[int(x) for x in list(line.strip())]]

            for i in range(1, 5):
                lst.append([increment(lst[i - 1][j]) for j in range(len(lst[0]))])
            added = []
            for added_lst in lst:
                added.extend(added_lst)

            matrix.append(added)

        origin_height = len(matrix)

        for _ in range(4):
            for _ in range(origin_height):
                m = len(matrix)
                matrix.append([increment(matrix[m - origin_height][j]) for j in range(len(matrix[0]))])

        return dijkstra(matrix)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
