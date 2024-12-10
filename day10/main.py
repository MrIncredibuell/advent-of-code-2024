lines = open("input.txt").read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        data[(x, y)] = int(c)

def score(data, x, y, n):
    if n == 10:
        return {(x, y)}
    result = set()
    for (nx, ny) in [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1),
    ]:
        if data.get((nx, ny), -1) == n:
            result |= score(data, nx, ny, n+1)
    return result

def part1(data):
    s = 0
    for (x, y), value in data.items():
        if value == 0:
            a = score(data, x, y, 1)
            s += len(a)
    return s


def score2(data, x, y, n):
    if n == 10:
        return 1
    result = 0
    for (nx, ny) in [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1),
    ]:
        if data.get((nx, ny), -1) == n:
            result += score2(data, nx, ny, n+1)
    return result

def part2(data):
    s = 0
    for (x, y), value in data.items():
        if value == 0:
            a = score2(data, x, y, 1)
            s += a
    return s

print(part1(data))
print(part2(data))