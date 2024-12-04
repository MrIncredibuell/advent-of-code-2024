lines = open("input.txt").read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        data[(x, y)] = c


def part1(data):
    c = 0
    width = max(x for x, _ in data.keys()) + 1
    height = max(y for y, _ in data.keys()) + 1
    for x in range(width):
        for y in range(height):
            for dx, dy in (
                (0,1),
                (0,-1),
                (1, 0),
                (-1, 0),
                (1, 1),
                (1,-1),
                (-1, 1),
                (-1, -1),
            ):
                s = ""
                for i in range(4):
                    s += data.get((x + (i * dx), y + (i * dy)), ".")
                if s == "XMAS":
                    c += 1
    return c


def part2(data):
    c = 0
    width = max(x for x, _ in data.keys()) + 1
    height = max(y for y, _ in data.keys()) + 1
    for x in range(width):
        for y in range(height):
            s1 = data.get((x+1, y+1), ".") + data.get((x, y), ".") + data.get((x-1, y-1), ".")
            s2 = data.get((x-1, y+1), ".") + data.get((x, y), ".") + data.get((x+1, y-1), ".")
                
            if (s1 == "MAS" or s1 == "SAM") and (s2 == "MAS" or s2 == "SAM"):
                c += 1
    return c

# print(part1(data))
print(part2(data))