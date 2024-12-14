from collections import defaultdict

lines = open("input.txt").read().split("\n")
data = []
for line in lines:
    p, v = line.split(" ")
    px, py = p[2:].split(",")
    vx, vy = v[2:].split(",")
    data.append(((int(px), int(py)), (int(vx), (int(vy)))))

def part1(data):
    INTERATIONS = 100
    WIDTH = 101
    HEIGHT = 103
    grid = defaultdict(list)
    for p,v in data:
        grid[p].append(v)
    for _ in range(INTERATIONS):
        new_grid = defaultdict(list)
        for (x, y), robots in grid.items():
            for (dx, dy) in robots:
                new_grid[((x + dx) % WIDTH, (y + dy) % HEIGHT)].append((dx, dy))
        grid = new_grid

    nw, ne, se, sw = 0, 0, 0, 0
    meridian = WIDTH // 2
    equator = HEIGHT // 2
    for (x, y), robots in grid.items():
        if x < meridian and y < equator:
            nw += len(robots)
        if x > meridian and y < equator:
            ne += len(robots)
        if x > meridian and y > equator:
            se += len(robots)
        if x < meridian and y > equator:
            sw += len(robots)

    return nw * ne * se * sw


def print_grid(grid, WIDTH, HEIGHT):
    s = ""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x,y) in grid:
                s += "*"
            else:
                s += " "
        s += "\n"
    return s


def score(grid, WIDTH):
    s = 0
    for (x,y) in grid.keys():
        if WIDTH // 3 < x < (2 * WIDTH) // 3:
            s += 1
    return s
    


def part2(data):
    WIDTH = 101
    HEIGHT = 103
    grid = defaultdict(list)
    for p,v in data:
        grid[p].append(v)
    i = 1
    best = 0
    while True:
        new_grid = defaultdict(list)
        for (x, y), robots in grid.items():
            for (dx, dy) in robots:
                new_grid[((x + dx) % WIDTH, (y + dy) % HEIGHT)].append((dx, dy))
        grid = new_grid
        s = score(grid, WIDTH=WIDTH)
        if s > best:
            best = s
            print(print_grid(grid, WIDTH=WIDTH, HEIGHT=HEIGHT))
            print(i)
            print()
            if input() == "q":
                return i
        i += 1

print(part1(data))
print(part2(data))
