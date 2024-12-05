from collections import defaultdict

parts = open("input.txt").read().split("\n\n")
rules = defaultdict(set)
inverse_rules = defaultdict(set)

for line in parts[0].split("\n"):
    a, b = line.split("|")
    rules[a].add(b)
    inverse_rules[b].add(a)
updates = [line.split(",") for line in parts[1].split("\n")]


def part1(rules, updates):
    s = 0
    for update in updates:
        seen = set()
        ok = True
        for n in update:
            if seen & rules[n]:
                ok = False
            seen.add(n)
        if ok:
            s += int(update[int(len(update)/2)])

    return s


def part2(rules, inverse_rules, updates):
    incorrect = []
    for update in updates:
        seen = set()
        ok = True
        for n in update:
            if seen & rules[n]:
                ok = False
            seen.add(n)
        if not ok:
            incorrect.append(update)

    s = 0
    for update in incorrect:
        inverse_rules_copy = {
            n: inverse_rules[n] & set(update) for n in update
        }

        result = []
        while len(result) < len(update):
            for k, v in inverse_rules_copy.items():
                if k not in result and len(v - set(result)) == 0:
                    result.append(k)
        s += int(result[int(len(result)/2)])

    return s

print(part1(rules, updates))
print(part2(rules, inverse_rules, updates))