lines = open("input.txt").read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        data[(x, y)] = c

def part1(data):
    x, y = [key for key, value in data.items() if value == "^"][0]
    direction = "up"
    seen = set()
    while (x,y) in data:
        seen.add((x,y))
        if direction == "up":
            if data.get((x,y-1), ".") == "#":
                direction = "right"
            else:
                y -= 1
        elif direction == "right":
            if data.get((x+1,y), ".") == "#":
                direction = "down"
            else:
                x += 1
        elif direction == "down":
            if data.get((x,y+1), ".") == "#":
                direction = "left"
            else:
                y += 1
        elif direction == "left":
            if data.get((x-1,y), ".") == "#":
                direction = "up"
            else:
                x -= 1

    return len(seen)


def get_path(data, x, y, direction):
    seen = set()
    while (x,y) in data:
        seen.add((x,y))
        if direction == "up":
            if data.get((x,y-1), ".") == "#":
                direction = "right"
            else:
                y -= 1
        elif direction == "right":
            if data.get((x+1,y), ".") == "#":
                direction = "down"
            else:
                x += 1
        elif direction == "down":
            if data.get((x,y+1), ".") == "#":
                direction = "left"
            else:
                y += 1
        elif direction == "left":
            if data.get((x-1,y), ".") == "#":
                direction = "up"
            else:
                x -= 1
    return seen

def check_for_loop(data, x, y, direction):
    seen = set()
    while (x,y) in data:
        if ((x,y), direction) in seen:
            return True
        seen.add(((x,y), direction))
        if direction == "up":
            if data.get((x,y-1), ".") == "#":
                direction = "right"
            else:
                y -= 1
        elif direction == "right":
            if data.get((x+1,y), ".") == "#":
                direction = "down"
            else:
                x += 1
        elif direction == "down":
            if data.get((x,y+1), ".") == "#":
                direction = "left"
            else:
                y += 1
        elif direction == "left":
            if data.get((x-1,y), ".") == "#":
                direction = "up"
            else:
                x -= 1
    return False

def part2(data):
    x, y = [key for key, value in data.items() if value == "^"][0]
    direction = "up"

    obstacles = set()
    potentials = get_path(data, x, y, direction) - {x, y}
    for p in potentials:
        data[p] = "#"
        if check_for_loop(data, x, y, direction):
            obstacles.add(p)
        data[p] = "."

    return len(obstacles)
    


print(part1(data))
print(part2(data))