from math import inf

data = open("input.txt").read().split("\n")

grid1 = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

grid2 = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


def valid_permuations(values, x, y, dx, dy):
    if (x == dx) and (y == dy):
        yield "A"
        return
    if x < dx and (x + 1, y) in values:
        for p in valid_permuations(values, x+1, y, dx, dy):
            yield ">" + p
    if x > dx and (x - 1, y) in values:
        for p in valid_permuations(values, x-1, y, dx, dy):
            yield "<" + p
    if y < dy and (x, y + 1) in values:
        for p in valid_permuations(values, x, y+1, dx, dy):
            yield "v" + p
    if y > dy and (x, y - 1) in values:
        for p in valid_permuations(values, x, y-1, dx, dy):
            yield "^" + p


def f(grid, x, y, sequence):
    if len(sequence) == 0:
        yield ""
        return

    dx, dy = grid.get(sequence[0])
    for p in valid_permuations(set(grid.values()), x, y, dx, dy):
        for p2 in f(grid, dx, dy, sequence[1:]):
            yield p + p2


def expand(start, dest):
    best = inf
    for r1 in f(grid1, *start, dest):
        for r2 in f(grid2, *grid2["A"], r1):
            for r3 in f(grid2, *grid2["A"], r2):
                if len(r3) < best:
                    best = len(r3)
    return best


def part1(data):
    score = 0
    for line in data[:]:
        complexity = 0
        start = grid1["A"]
        for c in line:
            complexity += expand(start, c)
            start = grid1[c]

        score += int(line[:3]) * complexity
    return score

def part2(data):
    score = 0
    for line in data[:]:
        complexity = 0
        start = grid1["A"]
        for c in line:
            complexity += expand(start, c)
            start = grid1[c]

        score += int(line[:3]) * complexity
    return score

print(part1(data))
# print(part2(data))