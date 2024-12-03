data = open("input.txt").read()


def part1(data):
    total = 0
    splits = data.split("mul(")[1:]
    for s in splits:
        if ")" in s:
            content = s.split(")")[0]
            try:
                a, b = content.split(",")
                total += int(a) * int(b)
            except:
                pass
    return total


def part2(data):
    total = 0
    do = True
    i = 0
    while i < len(data):
        if data[i:].startswith("do()"):
            do = True
            i += len("do()")
        elif data[i:].startswith("don't()"):
            do = False
            i += len("don't()")
        elif data[i:].startswith("mul("):
            i += len("mul(")
            content = data[i:].split(")")[0]
            try:
                a, b = content.split(",")
                if do:
                    total += int(a) * int(b)
                i += len(content)
            except:
                pass
        else:
            i += 1
    return total

        

# print(part1(data))
print(part2(data))