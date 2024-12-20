from heapq import heappush, heappop
from math import inf
from collections import defaultdict

lines = open("input.txt").read().split("\n")

data = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        data[(x, y)] = c

def neighbors(grid):
    ns = defaultdict(set)
    for (x,y), v in grid.items():
        if v == "#":
            continue
        for n in (
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
        ):
            if grid.get(n) in (".", "E", "S"):
                ns[(x,y)].add((n, 1))
    return ns

def bfs(edges, start, end):
    distances = {}
    to_visit = []
    to_visit_set = set([start])
    heappush(to_visit, (0, start))
    while to_visit:
        d, node = heappop(to_visit)
        if node == end:
            return d, distances
        to_visit_set.remove(node)
        for n, weight in edges[node]:
            if n not in to_visit_set and n not in distances:
                heappush(to_visit, (d+weight, n))
                to_visit_set.add(n)
        distances[node] = d


def part1(data):
    start = next(k for k, v in data.items() if v == "S")
    end = next(k for k, v in data.items() if v == "E")
    edges = neighbors(data)
    savings = defaultdict(set)
    fair_score, reachable = bfs(edges, start, end)
    _, reverse_reachable = bfs(edges, end, start)
    for (x, y), dist in reachable.items():
        for i in range(2, 3):
            for j in range(i + 1):
                if (cheat_score := reverse_reachable.get((x + j, y + (i - j)), inf) + dist + i) < fair_score:
                    savings[fair_score - cheat_score].add(((x,y), (x + j, y + (i - j))))
                if (cheat_score := reverse_reachable.get((x - j, y + (i - j)), inf) + dist + i) < fair_score:
                    savings[fair_score - cheat_score].add(((x,y), (x - j, y + (i - j))))
                if (cheat_score := reverse_reachable.get((x + j, y - (i - j)), inf) + dist + i) < fair_score:
                    savings[fair_score - cheat_score].add(((x,y), (x + j, y - (i - j))))
                if (cheat_score := reverse_reachable.get((x - j, y - (i - j)), inf) + dist + i) < fair_score:
                    savings[fair_score - cheat_score].add(((x,y), (x - j, y - (i - j))))

    savings = {k: len(v) for k, v in savings.items()}
    return sum(v for k, v in savings.items() if k >= 100)

def part2(data):
    start = next(k for k, v in data.items() if v == "S")
    end = next(k for k, v in data.items() if v == "E")
    edges = neighbors(data)
    savings = defaultdict(set)
    fair_score, reachable = bfs(edges, start, end)
    _, reverse_reachable = bfs(edges, end, start)
    for (x, y), dist in reachable.items():
        for i in range(2, 21):
            for j in range(i + 1):
                if (cheat_score := reverse_reachable.get((x + j, y + (i - j)), inf) + dist + i) < fair_score:
                    savings[fair_score - cheat_score].add(((x,y), (x + j, y + (i - j))))
                if (cheat_score := reverse_reachable.get((x - j, y + (i - j)), inf) + dist + i) < fair_score:
                    savings[fair_score - cheat_score].add(((x,y), (x - j, y + (i - j))))
                if (cheat_score := reverse_reachable.get((x + j, y - (i - j)), inf) + dist + i) < fair_score:
                    savings[fair_score - cheat_score].add(((x,y), (x + j, y - (i - j))))
                if (cheat_score := reverse_reachable.get((x - j, y - (i - j)), inf) + dist + i) < fair_score:
                    savings[fair_score - cheat_score].add(((x,y), (x - j, y - (i - j))))

    savings = {k: len(v) for k, v in savings.items()}
    return sum(v for k, v in savings.items() if k >= 100)


print(part1(data))
print(part2(data))