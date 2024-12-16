from heapq import heappush, heappop
from math import inf

lines = open("input.txt").read().split("\n")

data = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        data[(x, y)] = c

EAST, NORTH, WEST, SOUTH = "EAST", "NORTH", "WEST", "SOUTH"

def generate_neighbors(distance, location, direction):
    x,y = location

    if direction == EAST:
        yield (distance + 1, (x + 1, y), EAST)
        yield (distance + 1000, (x,y), NORTH)
        yield (distance + 1000, (x,y), SOUTH)
    elif direction == NORTH:
        yield (distance + 1, (x, y + 1), NORTH)
        yield (distance + 1000, (x,y), EAST)
        yield (distance + 1000, (x,y), WEST)
    elif direction == WEST:
        yield (distance + 1, (x - 1, y), WEST)
        yield (distance + 1000, (x,y), NORTH)
        yield (distance + 1000, (x,y), SOUTH)
    elif direction == SOUTH:
        yield (distance + 1, (x, y - 1), SOUTH)
        yield (distance + 1000, (x,y), EAST)
        yield (distance + 1000, (x,y), WEST)



def part1(data):
    start = next(k for k, v in data.items() if v == "S")
    end = next(k for k, v in data.items() if v == "E")

    distances = {}
    to_visit = []
    heappush(to_visit, (0, start, EAST))
    while to_visit:
        dist, location, direction = heappop(to_visit)
        if data[location] == "#" :
            continue
        if distances.get((location, direction), inf) > dist:
            distances[(location, direction)] = dist
            for n in generate_neighbors(dist, location, direction):
                heappush(to_visit, n)

    r = min(distances.get((end, d), inf) for d in (EAST, NORTH, WEST, SOUTH))
    return r


def generate_neighbors2(distance, location, direction):
    x,y = location

    if direction == EAST:
        yield (distance + 1, (x + 1, y), EAST, (location, EAST))
        yield (distance + 1000, (x,y), NORTH, (location, EAST))
        yield (distance + 1000, (x,y), SOUTH, (location, EAST))
    elif direction == NORTH:
        yield (distance + 1, (x, y + 1), NORTH, (location, NORTH))
        yield (distance + 1000, (x,y), EAST, (location, NORTH))
        yield (distance + 1000, (x,y), WEST, (location, NORTH))
    elif direction == WEST:
        yield (distance + 1, (x - 1, y), WEST, (location, WEST))
        yield (distance + 1000, (x,y), NORTH, (location, WEST))
        yield (distance + 1000, (x,y), SOUTH, (location, WEST))
    elif direction == SOUTH:
        yield (distance + 1, (x, y - 1), SOUTH, (location, SOUTH))
        yield (distance + 1000, (x,y), EAST, (location, SOUTH))
        yield (distance + 1000, (x,y), WEST, (location, SOUTH))

def part2(data):
    start = next(k for k, v in data.items() if v == "S")
    end = next(k for k, v in data.items() if v == "E")

    distances = {}
    paths = {}
    to_visit = []
    heappush(to_visit, (0, start, EAST, None))
    while to_visit:
        dist, location, direction, source = heappop(to_visit)
        if data[location] == "#" :
            continue
        if distances.get((location, direction), inf) == dist:
            paths[(location, direction)].add(source)
        elif distances.get((location, direction), inf) > dist:
            distances[(location, direction)] = dist
            paths[(location, direction)] = set([source])

            for n in generate_neighbors2(dist, location, direction):
                heappush(to_visit, n)

    on_path = set([end])
    to_visit = set()
    visited = set()
    end_distance = min([distances.get((end, d)) for d in (EAST, NORTH, WEST, SOUTH)])
    for d in (EAST, NORTH, WEST, SOUTH):
        dist = distances.get((end, d))

        if dist == end_distance and (sources := paths.get((end, d), None)):
            to_visit |= sources

    while to_visit:
        (ll, d) = to_visit.pop()
        if (ll, d) in visited:
            continue
        visited.add((ll,d))
        on_path.add(ll)
        if to_add := paths.get((ll,d), set()):
            to_visit |= {a for a in to_add if a}

    return len(on_path)

print(part1(data))
print(part2(data))