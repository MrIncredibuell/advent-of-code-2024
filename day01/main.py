lines = open("input.txt").read().split("\n")
data = ([],[])
for line in lines:
    a, b = line.split("   ")
    data[0].append(int(a))
    data[1].append(int(b))

def part1(data):
    s = 0
    a = sorted(data[0])
    b = sorted(data[1])
    for i, x in enumerate(a):
        s += abs(x - b[i])
    return s


def part2(data):
    s = 0
    for x in data[0]:
        s += (x * data[1].count(x))
    return s

print(part1(data))
print(part2(data))