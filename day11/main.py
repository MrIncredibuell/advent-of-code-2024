from functools import lru_cache
from collections import defaultdict

data = [int(x) for x in open("input.txt").read().split(" ")]

        
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next_node: "Node" = None

    def __len__(self):
        result = 1
        n = self.next_node
        while n is not None:
            result +=1
            n = n.next_node
        return result

    def __repr__(self):
        s = str(self.value)
        if self.next_node is not None:
            s += f" {self.next_node}" 
        return s


def part1(data):
    l = Node(data[0])
    c = l
    for stone in data[1:]:
        c.next_node = Node(stone)
        c = c.next_node

    for i in range(25):
        length = 0
        c = l
        while c is not None:
            length += 1
            if c.value == 0:
                c.value = 1
            elif len(str_value := str(c.value)) % 2 == 0:
                a = int(str_value[:len(str_value) // 2])
                b = int(str_value[len(str_value) // 2:])
                c.next_node = Node(b, next_node=c.next_node)
                c.value = a
                c = c.next_node
                length += 1
            else:
                c.value *= 2024
            c = c.next_node

    return length


@lru_cache(maxsize=1000000)
def go(stone):
    if stone == 0:
        return [1]
    elif len(str_value := str(stone)) % 2 == 0:
        a = int(str_value[:len(str_value) // 2])
        b = int(str_value[len(str_value) // 2:])
        return [a, b]
    return [stone *  2024]

def part2(data):
    stones = {s: data.count(s) for s in data}
    for i in range(75):
        new_stones = defaultdict(int)
        for s, c in stones.items():
            for r in go(s):
                new_stones[r] += c
        stones = new_stones

    return sum(stones.values())

print(part1(data))
print(part2(data))