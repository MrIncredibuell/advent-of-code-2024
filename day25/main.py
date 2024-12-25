chunks = open("input.txt").read().split("\n\n")
locks = []
keys = []

for chunk in chunks:
    lines = chunk.split()
    is_key = lines[0] != "#####"
    sizes = [0] * 5
    for line in lines[1:-1]:
        for i, c in enumerate(line):
            if c == "#":
                sizes[i] += 1
    if is_key:
        keys.append(sizes)
    else:
        locks.append(sizes)

def part1(keys, locks):
    s = 0
    for k in keys:
        for l in locks:
            valid = True
            for i in range(5):
                if k[i] + l[i] > 5:
                    valid = False
            if valid:
                s += 1

    return s


def part2(data):
    s = 0
    for x in data[0]:
        s += (x * data[1].count(x))
    return s

print(part1(keys, locks))
# print(part2(data))