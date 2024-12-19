from heapq import heappush, heappop

lines = open("input.txt").read().split("\n")

data = {}
for line in lines[:1024]:
    data[tuple(int(x) for x in line.split(","))] = "#"

data2 = []
for line in lines:
    data2.append(tuple(int(x) for x in line.split(",")))

def part1(data):

    for i in range(71):
        for j in range(71):
            data[(i,j)] = data.get((i,j), ".")
    
    visited = {}
    to_visit = []
    heappush(to_visit, (0, (0,0)))
    to_visit_set = {(0,0)}
    while to_visit:
        distance, (x,y) = heappop(to_visit)
        to_visit_set.remove((x,y))
        for n in (
            (x-1,y),
            (x+1,y),
            (x,y-1),
            (x,y+1),
        ):
            if (data.get(n, "#") != "#") and (n not in visited) and (n not in to_visit_set):
                heappush(to_visit, (distance + 1, n))
                to_visit_set.add(n)
        visited[(x,y)] = distance
    return visited[(70,70)]


def solve(data):
    for i in range(71):
        for j in range(71):
            data[(i,j)] = data.get((i,j), ".")
    
    visited = {}
    to_visit = []
    heappush(to_visit, (0, (0,0)))
    to_visit_set = {(0,0)}
    while to_visit:
        distance, (x,y) = heappop(to_visit)
        to_visit_set.remove((x,y))
        for n in (
            (x-1,y),
            (x+1,y),
            (x,y-1),
            (x,y+1),
        ):
            if (data.get(n, "#") != "#") and (n not in visited) and (n not in to_visit_set):
                heappush(to_visit, (distance + 1, n))
                to_visit_set.add(n)
        visited[(x,y)] = distance
    return visited.get((70,70), None)


def part2(data):
    a = 1
    while True:
        grid = {k: "#" for k in data[:a]}
        if (solve(grid)) is None:
            return data[a-1]
        a += 1

print(part1(data))
print(part2(data2))