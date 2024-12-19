chunks = open("input.txt").read().split("\n\n")
towels = chunks[0].split(", ")
data = chunks[1].split("\n")


def solve(towels, row):
    m = max((len(t) for t in towels))
    scores = [0] * len(row)
    for j in range(m):
        if row[:j+1] in towels:
            scores[j] = 1
    for i in range(1, len(row)):
        for j in range(m):
            if i - j > 0 and row[i-j:i+1] in towels:
                scores[i] += scores[i-j-1]
    return scores[-1]


def part1(towels, data):
    s = 0
    towels = set(towels)
    for row in data:
        if not row:
            continue
        if solve(towels, row):
            s += 1
    return s


def part2(towels, data):
    s = 0
    towels = set(towels)
    for row in data:
        if not row:
            continue
        s += solve(towels, row)
    return s

print(part1(towels, data))
print(part2(towels, data))