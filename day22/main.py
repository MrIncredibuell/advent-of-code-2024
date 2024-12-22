data = [int(x) for x in open("input.txt").read().split("\n") if x]

def mix(x, secret):
    return x ^ secret

def prune(secret):
    return secret % 16777216

def evolve(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix((secret // 32), secret))
    secret = prune(mix(secret * 2048, secret))
    return secret

    
def part1(data):
    s = 0
    for x in data:
        y = x
        for _ in range(2000):
            y = evolve(y)
        s += y
    return s


def part2(data):
    all_scores = []
    for x in data:
        y = x
        seq = (None, None, None, None)
        scores = {}
        for _ in range(2000):
            new_y = evolve(y)
            d = (new_y % 10) - (y % 10)
            new_seq = (seq[1], seq[2], seq[3], d)
            if (None not in new_seq) and new_seq not in scores:
                scores[new_seq] = new_y % 10
            y = new_y
            seq = new_seq
        all_scores.append(scores)

    ks = set()
    for scores in all_scores:
        ks |= set(scores.keys())
     
    best = 0
    for k in ks:
        s = 0
        for score in all_scores:
            s += score.get(k, 0)
        if s > best:
            best = s

    return best

print(part1(data))
print(part2(data))