lines = open("input.txt").read().split("\n")
data = []
for line in lines:
    a, b = line.split(": ")
    data.append((int(a), [int(x) for x in b.split(" ")]))

def solve(ans, current, remaining):
    n = remaining[0]
    if len(remaining) == 1:
        if current + n == ans or current * n == ans:
            return True
        return False
    return solve(ans, current + n, remaining[1:]) or solve(ans, current * n, remaining[1:])


def part1(data):
    s = 0
    for a, b in data:
        if solve(a, b[0], b[1:]):
            s += a
    return s

def solve2(ans, current, remaining):
    n = remaining[0]
    if len(remaining) == 1:
        if (current + n == ans) or (current * n == ans) or (int(str(current) + str(n)) == ans):
            return True
        return False
    return solve2(ans, current + n, remaining[1:]) or solve2(ans, current * n, remaining[1:]) or solve2(ans, int(str(current) + str(n)), remaining[1:])

def part2(data):
    s = 0
    for a, b in data:
        if solve2(a, b[0], b[1:]):
            s += a
    return s

print(part1(data))
print(part2(data))