lines = open("input.txt").read().split("\n")
data = [[int(x) for x in line.split(" ")] for line in lines]

def is_safe(line):
    for i, x in enumerate(line[:-1]):
        if (d := abs(x - line[i+1])) > 3 or d == 0:
            return False
        
    for i, x in enumerate(line[:-2]):
        if x - line[i+1] < 0 and line[i+1] - line[i+2] > 0:
            return False
        if x - line[i+1] > 0 and line[i+1] - line[i+2] < 0:
            return False
    
    return True


def part1(data):
    s = 0
    for line in data:
        if is_safe(line):
            s += 1 
    return s


def part2(data):
    s = 0
    for line in data:
        sub_lines = [line] + [line[:x] + line[x+1:] for x in range(len(line))]

        for sub in sub_lines:
            if is_safe(sub):
                s += 1
                break
    return s

# print(part1(data))
print(part2(data))