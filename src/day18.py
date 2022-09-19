from json import loads
from math import floor, ceil

# https://adventofcode.com/2021/day/18
input = "data/input18.txt"


class Node:
    def __init__(self, left, right, parent=None):
        self.parent = parent
        if type(left) != list:  # int / node
            self.left = left
            if type(self.left) == Node:
                self.left.set_parent(self)
        else:
            self.left = Node(left[0], left[1], self)

        if type(right) != list:  # int / node
            self.right = right

            if type(self.right) == Node:
                self.right.set_parent(self)
        else:
            self.right = Node(right[0], right[1], self)

    def add_to_left(self, val):
        p = self.parent

        if p.get_left() == self:
            p0 = p
            p = p.parent

            while p is not None:
                if p.get_left() != p0:
                    break
                p0 = p
                p = p.parent

        if p is not None:
            if type(p.get_left()) == int:
                p.set_left(p.get_left() + val)
            else:
                p = p.get_left()

                while type(p.get_right()) != int:
                    p = p.get_right()
                p.set_right(p.get_right() + val)

    def add_to_right(self, val):
        p = self.parent
        if p.get_right() == self:
            p0 = p
            p = p.parent

            while p is not None:
                if p.get_right() != p0:
                    break
                p0 = p
                p = p.parent
        if p is not None:
            if type(p.get_right()) == int:
                p.set_right(p.get_right() + val)
            else:
                p = p.get_right()

                while type(p.get_left()) != int:
                    p = p.get_left()
                p.set_left(p.get_left() + val)

    def add_from_explosion(self):
        l_val = self.left
        r_val = self.right
        parent = self.parent

        self.add_to_right(r_val)
        self.add_to_left(l_val)

        if parent.get_left() is self:
            parent.set_left(0)
        elif parent.get_right() is self:
            parent.set_right(0)

    def explode(self, h=0):
        if type(self.left) == int and type(self.right) == int:
            if h >= 4:
                self.add_from_explosion()
                return True
        if type(self.left) == Node:
            if self.left.explode(h + 1):
                return True
        if type(self.right) == Node:
            if self.right.explode(h + 1):
                return True
        return False

    def split(self):
        if type(self.left) == int:
            if self.left > 9:
                a = floor(self.left / 2)
                b = ceil(self.left / 2)
                self.left = Node(a, b, self)
                return True
        if type(self.left) == Node:
            if self.left.split():
                return True

        if type(self.right) == int:
            if self.right > 9:
                a = floor(self.right / 2)
                b = ceil(self.right / 2)
                self.right = Node(a, b, self)
                return True
        if type(self.right) == Node:
            if self.right.split():
                return True
        return False

    def __add__(self, other):
        x = Node(self, other)
        # x.postorder(); print("initial")
        ok = False
        while not ok:
            ok = True
            if x.height() > 4:
                x.explode()
                ok = False
                # x.postorder(); print("boom")
                continue
            if x.split():
                # x.postorder(); print("split")
                ok = False

        return x

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent

    def magnitude(self) -> int:
        mag = 0
        if type(self.left) == int:
            mag += 3 * self.left
        else:
            mag += 3 * self.left.magnitude()

        if type(self.right) == int:
            mag += 2 * self.right
        else:
            mag += 2 * self.right.magnitude()

        return mag

    def height(self) -> int:
        if type(self.left) == int and type(self.right) == int:
            return 1
        if type(self.left) == Node and type(self.right) == Node:
            return 1 + max(self.left.height(), self.right.height())
        if type(self.left) == Node:
            return 1 + self.left.height()
        if type(self.right) == Node:
            return 1 + self.right.height()

    def postorder(self):
        if type(self.get_left()) == int:
            print(f"{self.get_left()}", end=" ")
        else:
            self.get_left().postorder()

        if type(self.get_right()) == int:
            print(f"{self.get_right()}", end=" ")
        else:
            self.get_right().postorder()


def part1():
    with open(input, 'r') as file:
        lst = []
        for line in file:
            string = loads(line.strip())
            snailfish_number = Node(string[0], string[1])
            lst.append(snailfish_number)

        snail_sum = lst[0]
        for i in range(1, len(lst)):
            snail_sum = snail_sum + lst[i]
        return snail_sum.magnitude()


def part2():
    with open(input, 'r') as file:
        lst = []
        for line in file:
            string = loads(line.strip())
            lst.append(string)

        max_magnitude = float("-inf")

        for i in range(len(lst)):
            for j in range(len(lst)):
                if i != j:
                    n1 = Node(lst[i][0], lst[i][1])
                    n2 = Node(lst[j][0], lst[j][1])
                    k = (n1 + n2).magnitude()
                    if k > max_magnitude:
                        max_magnitude = k

        return max_magnitude


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
