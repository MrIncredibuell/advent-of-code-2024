from collections import defaultdict

lines = open("input.txt").read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        data[(x, y)] = c

def part1(data):
    groups = defaultdict(set)
    s = set()
    for k, v in data.items():
        if v != ".":
            groups[v].add(k)

    for k, vs in groups.items():
        while vs:
            (x,y) = vs.pop()
            for (a,b) in vs:
                dx = x - a
                dy = y - b
                if data.get((x + dx, y + dy), " ") != " ":
                    s.add((x + dx, y + dy))
                if data.get((a - dx, b - dy), " ") != " ":
                    s.add((a - dx, b - dy))
    return len(s)


def part2(data):
    groups = defaultdict(set)
    s = set()
    for k, v in data.items():
        if v != ".":
            groups[v].add(k)

    for k, vs in groups.items():
        while vs:
            (x,y) = vs.pop()
            for (a,b) in vs:
                dx = x - a
                dy = y - b
                done = False
                i = 0
                while not done:
                    done = True
                    if data.get(((m := x + dx * i), n := (y + dy * i)), " ") != " ":
                        s.add((m, n))
                        done = False
                    if data.get(((m := x - dx * i), n := (y - dy * i)), " ") != " ":
                        s.add((m, n))
                        done = False
                    i += 1
    print(sorted(s))
    return len(s)

# print(part1(data))
print(part2(data))