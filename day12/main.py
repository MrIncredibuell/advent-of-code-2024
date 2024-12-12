lines = open("input.txt").read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        data[(x, y)] = c

def part1(data):
    s = 0
    unvisited = {k for k in data.keys()}
    while unvisited:
        node = unvisited.pop()
        to_visit = set()
        to_visit.add(node)
        area = 0
        perimeter = 0
        v = data[node]
        visited = set()
        
        while to_visit:
            (x,y) = to_visit.pop()
            visited.add((x,y))
            area +=1
            for neighbor in ((
                (x+1,y),
                (x-1,y),
                (x,y+1),
                (x,y-1),
            )):
                if neighbor not in visited:
                    if data.get(neighbor, None) == v:
                        to_visit.add(neighbor)
                    else:
                        perimeter += 1
        unvisited -= visited
        cost = area * perimeter
        s += cost
            
    return s


def part2(data):
    s = 0
    unvisited = {k for k in data.keys()}
    while unvisited:
        node = unvisited.pop()
        to_visit = set()
        to_visit.add(node)
        area = 0
        v = data[node]
        visited = set()

        edges = set()
        
        while to_visit:
            (x,y) = to_visit.pop()
            visited.add((x,y))
            area +=1
            for neighbor in ((
                (x+1,y),
                (x-1,y),
                (x,y+1),
                (x,y-1),
            )):
                if neighbor not in visited:
                    if data.get(neighbor, None) == v:
                        to_visit.add(neighbor)
                    else:
                        edges.add(tuple((((x,y), neighbor))))
        unvisited -= visited

        sides = 0
        while edges:
            ((x1, y1), (x2, y2)) = edges.pop()
            if x1 == x2:
                checked = set(((x1, y1), (x2, y2)))
                to_check = {((x1 - 1, y1), (x1 - 1, y2)), ((x1 + 1, y1), (x1 + 1, y2))}
                while to_check:
                    ((x3, y3), (x4, y4)) = to_check.pop()
                    if ((x3, y3), (x4, y4)) in edges:
                        edges.remove(((x3, y3), (x4, y4)))
                        to_check |= {((x3 - 1, y3), (x3 - 1, y4)), ((x3 + 1, y3), (x3 + 1, y4))}
                    checked.add(((x3, y3), (x4, y4)))
                    to_check -= checked
                sides += 1
            else:
                checked = set(((x1, y1), (x2, y2)))
                to_check = {((x1, y1 - 1), (x2, y1 - 1)), ((x1, y1 + 1), (x2, y2 + 1))}
                while to_check:
                    ((x3, y3), (x4, y4)) = to_check.pop()
                    if ((x3, y3), (x4, y4)) in edges:
                        edges.remove(((x3, y3), (x4, y4)))
                        to_check |= {((x3, y3 - 1), (x4, y4 - 1)), ((x3, y3 + 1), (x4, y4 + 1))}
                    checked.add(((x3, y3), (x4, y4)))
                    to_check -= checked
                sides += 1

        print(v, sides, area)

        cost = area * sides
        s += cost
            
    return s

# print(part1(data))
print(part2(data))