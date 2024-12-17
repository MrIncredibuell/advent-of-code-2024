from copy import copy

chunks = open("input.txt").read().split("\n\n")

grid = {}
for y, line in enumerate(chunks[0].split("\n")):
    for x, c in enumerate(line):
        grid[(x, y)] = c

moves = chunks[1].replace("\n", "")


def try_move(grid, location, direction):
    x, y = location
    if direction == "^":
        dest = (x, y - 1)
    elif direction == ">":
        dest = (x + 1, y)
    elif direction == "v":
        dest = (x, y + 1)
    elif direction == "<":
        dest = (x - 1, y)

    if (spot := grid[dest]) == ".":
        grid[dest] = grid[(x, y)]
        grid[(x, y)] = "."
        return dest, True
    elif spot == "O":
        _, can_move = try_move(grid, dest, direction)
        if can_move:
            grid[dest] = grid[(x, y)]
            grid[(x, y)] = "."
            return dest, True

    return location, False


def part1(grid, moves):
    (x, y) = next(k for k, v in grid.items() if v == "@")
    for move in moves:
        (x, y), _ = try_move(grid, (x, y), move)

    s = 0
    for (i, j), v in grid.items():
        if v == "O":
            s += (100 * j) + i
    return s


def can_move(grid, location, direction):
    x, y = location
    dx, dy = 0, 0
    if direction == "^":
        dy = -1
    elif direction == ">":
        dx = 1
    elif direction == "v":
        dy = 1
    elif direction == "<":
        dx = -1

    if (spot := grid[(x + dx, y + dy)]) == ".":
        return True
    elif spot == "[":
        if direction == ">":
            return can_move(grid, (x + dx + 1, y), direction)
        elif direction == "<":
            raise NotImplementedError("SHOULD BE IMPOSSIBLE")
        else:
            return can_move(grid, (x, y + dy), direction) and can_move(
                grid, (x + 1, y + dy), direction
            )
    elif spot == "]":
        if direction == ">":
            raise NotImplementedError("SHOULD BE IMPOSSIBLE")
        elif direction == "<":
            return can_move(grid, (x + dx - 1, y), direction)
        else:
            return can_move(grid, (x, y + dy), direction) and can_move(
                grid, (x - 1, y + dy), direction
            )

    return False


def do_move(grid, location, direction):
    if grid[location] == ".":
        return

    x, y = location
    dx, dy = 0, 0
    if direction == "^":
        dy = -1
    elif direction == ">":
        dx = 1
    elif direction == "v":
        dy = 1
    elif direction == "<":
        dx = -1

    if (spot := grid[(x + dx, y + dy)]) == ".":
        pass
    elif spot == "[":
        if direction == ">":
            do_move(grid, (x + dx + 1, y), direction)
            grid[(x + 2 * dx, y)] = "["
            grid[(x + 3 * dx, y)] = "]"
            grid[(x + dx, y + dy)] = "."
        elif direction == "<":
            raise NotImplementedError("SHOULD BE IMPOSSIBLE")
        else:
            do_move(grid, (x, y + dy), direction)
            do_move(grid, (x + 1, y + dy), direction)
            grid[(x, y + 2 * dy)] = "["
            grid[(x + 1, y + 2 * dy)] = "]"
            grid[(x, y + dy)] = "."
            grid[(x + 1, y + dy)] = "."
    elif spot == "]":
        if direction == ">":
            raise NotImplementedError("SHOULD BE IMPOSSIBLE")
        elif direction == "<":
            do_move(grid, (x + dx - 1, y), direction)
            grid[(x + 2 * dx, y)] = "]"
            grid[(x + 3 * dx, y)] = "["
            grid[(x + dx, y + dy)] = "."
        else:
            do_move(grid, (x, y + dy), direction)
            do_move(grid, (x - 1, y + dy), direction)
            grid[(x, y + 2 * dy)] = "]"
            grid[(x - 1, y + 2 * dy)] = "["
            grid[(x, y + dy)] = "."
            grid[(x - 1, y + dy)] = "."
    grid[(x + dx, y + dy)] = grid[(x,y)]
    grid[(x,y)] = "."

    return (x + dx, y + dy)


def print_grid(grid):
    width, height = max(grid.keys())
    width += 1
    height += 1
    s = ""
    for i in range(height):
        for j in range (width):
            s += grid.get((j, i), "?")
        s += "\n"
    print(s)
    

def part2(grid, moves):
    new_grid = {}
    for (x, y), v in grid.items():
        if v == "#":
            new_grid[((2 * x), y)] = "#"
            new_grid[((2 * x) + 1, y)] = "#"
        elif v == "O":
            new_grid[((2 * x), y)] = "["
            new_grid[((2 * x) + 1, y)] = "]"
        elif v == ".":
            new_grid[((2 * x), y)] = "."
            new_grid[((2 * x) + 1, y)] = "."
        elif v == "@":
            new_grid[((2 * x), y)] = "@"
            new_grid[((2 * x) + 1, y)] = "."
    grid = new_grid
    (x, y) = next(k for k, v in grid.items() if v == "@")

    for move in moves[:]:
        if can_move(grid, (x, y), move):
            x, y = do_move(grid, (x, y), move)

    s = 0
    for (i, j), v in sorted(grid.items()):
        if v == "[":
            score = i + 100 * j
            s += score
    return s


print(part1(copy(grid), moves))
print(part2(copy(grid), moves))
