from math import inf

chunks = open("input.txt").read().split("\n\n")
data = []
for chunk in chunks:
    a, b, p = chunk.split("\n")
    ax, ay = a[len("Button A: "):].split(", ")
    ax, ay = int(ax[2:]), int(ay[2:])

    bx, by = b[len("Button B: "):].split(", ")
    bx, by = int(bx[2:]), int(by[2:])

    px, py = p[len("Prize: "):].split(", ")
    px, py = int(px[2:]), int(py[2:])

    data.append(((ax, ay), (bx, by), (px, py)))


def part1(data):
    s = 0
    for ((ax, ay), (bx, by), (px, py)) in data:
        best = inf
        for i in range(0, (px // bx) + 1):
            j = (px - (bx * i)) / (ax)
            if int(j) == j and ((ay * j) + (by * i) == py):
                j = int(j)
                best = min(best, i + (3*j)) 
        if best != inf:
            s += best
    return int(s)


def part2(data):
    s = 0
    for ((ax, ay), (bx, by), (px, py)) in data:
        px += 10000000000000
        py += 10000000000000
        j = ((px * ay) - (ax * py)) /  ((ay * bx) - (ax * by))
        i = (px - (bx * j)) / ax

        if j == int(j) and i == int(i):
            s += (i * 3 + j)

    return int(s)

print(part1(data))
print(part2(data))