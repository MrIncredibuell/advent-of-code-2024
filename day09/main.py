data = [int(c) for c in open("input.txt").read()]


def part1(data):
    s = []
    i = 0
    f = True
    for c in data:
        if f == True:
            s += [i] * c
        else:
            s += ["."] * c
        if f:
            i += 1
            f = False
        else:
            f = True

    n = 0
    z = len(s) - 1
    while n < z:
        while s[z] == ".":
            z -= 1
        while s[n] != ".":
            n += 1
        if n < z:
            s[n], s[z] = s[z], s[n]

    r = sum(i * x for i, x in enumerate(s[:z+1]))

    return r


from dataclasses import dataclass

@dataclass
class Node:
    prev: "Node" = None
    next: "Node" = None
    value: int | str = ""
    length: int = 0

def format(c):
    s = []
    while c is not None:
        s += [c.value] * c.length
        c = c.next
    return s

def part2(data):
    start = None
    current = None
    f = True
    i = 0
    for c in data:
        if f:
            current = Node(prev=current, next=None, value=i, length=c)
            i += 1
            f = False
        else:
            current = Node(prev=current, next=None, value=".", length=c)
            f = True
        if current.prev:
            current.prev.next = current
        if start is None:
            start = current
    end = current
    while end != None:
        # print(end.value, end.length)
        if end.value != ".":
            # print(end.value)
            free = start
            passed = False
            while free and (free.value != "." or free.length < end.length):
                if id(free) == id(end):
                    passed = True
                    break
                free = free.next
            if not passed and free and free.value == "." and free.length >= end.length:
                # print(end.value, free.value, free.length)
                new_end = Node(prev=free.prev, next=free, value=end.value, length=end.length)
                end.value = "."

                if free.prev:
                    free.prev.next = new_end
                free.prev = new_end
                free.length = free.length - end.length

                # end = start

        end = end.prev

    r = 0
    i = 0
    for c in format(start):
        # print(c)
        if c != ".":
            r += i * c
        i += 1
    return r




# print(part1(data))
print(part2(data))