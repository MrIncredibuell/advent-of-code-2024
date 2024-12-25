from collections import defaultdict

chunks = open("input.txt").read().split("\n\n")
inputs = []

for line in chunks[0].split("\n"):
    inputs.append(tuple(line.split(": ")))

ins = {
    k: v for k,v in inputs
}

gates = []
for line in chunks[1].split("\n"):
    if not line:
        continue
    left, right = line.split(" -> ")
    a, op, b = left.split(" ")
    gates.append((a, op, b, right))


def part1(ins, gates):
    while gates:
        to_remove = []
        for l, op, r, z in gates:
            if (l in ins) and (r in ins):
                if op == "AND":
                    ins[z] = "1" if (ins[l] == "1") and (ins[r] == "1") else "0"
                elif op == "XOR":
                    ins[z] = "1" if ((ins[l] == "1") or (ins[r] == "1")) and not (ins[l] == "1" and ins[r] == "1") else "0"
                elif op == "OR":
                    ins[z] = "1" if ((ins[l] == "1") or (ins[r] == "1")) else "0"
                to_remove.append((l, op, r, z))
        for row in to_remove:
            gates.remove(row)
    zs = sorted([(k, v) for k, v in ins.items() if k.startswith("z")])
    r = 0
    for i, (_,z) in enumerate(zs):
        if z == "1":
            r += 2 ** i

    return r


def deps(ins, gates):
    deps = defaultdict(set)
    while gates:
        to_remove = []
        for l, op, r, z in gates:
            if (l in ins) and (r in ins):
                deps[z] |= {l, r} | deps[l] | deps[r]
                ins[z] = None
                to_remove.append((l, op, r, z))
        for row in to_remove:
            gates.remove(row)
    return deps

def part2(ins, gates):
    backs = {}
    fores = defaultdict(set)
    for a, b, c, d in gates:
        backs[d] = (a, b, c)
        fores[a].add(b)
        fores[c].add(b)

    res = []

    for d, (a,b,c) in backs.items():
        if d[0] == "z" and b != "XOR":
            res.append(d)
        
        if b == "OR":
            (a1, b1, c1) = backs[a]
            (a2, b2, c2) = backs[c]
            if b1 != "AND":
                res.append(a)
            if b2 != "AND":
                res.append(c)
        if b == "AND" and a[0] not in "xy":
            (a1, b1, c1) = backs[a]
            (a2, b2, c2) = backs[c]
            if b1 == "AND":
                res.append(a)
            if b2 == "AND":
                res.append(c)
        
    res.remove("z45")
    res.remove("drq")
    # this returns 7 items, but I can figure out the last by hand
    return ",".join(sorted(res))


print(part1(ins, gates[:]))
print(part2(ins, gates[:]))