from collections import defaultdict
data = defaultdict(set)

lines = open("input.txt").read().split("\n")

for line in lines:
    if not line:
        continue
    a,b  = line.split("-")
    data[a].add(b)
    data[b].add(a)

def part1(data):
    triplets = set()
    for a, bs in data.items():
        for b in bs:
            for c in data[b]:
                if c != a and a in data[c]:
                    triplets.add(frozenset([a,b,c]))
                    
    return len([t for t in triplets if any((x[0] == "t" for x in t))])


def part2(data):
    nodes = data.keys()
    sets = set([frozenset([n]) for n in nodes])
    
    stop = False
    while not stop:
        result = sets
        stop = True
        new_sets = set()
        for s in sets:
            potentials = nodes
            for n in s:
                potentials &= data[n]
            for p in potentials:
                new_sets.add(frozenset([*s, p]))
                stop = False
        sets = new_sets

    return ",".join(sorted(result.pop()))

print(part1(data))
print(part2(data))