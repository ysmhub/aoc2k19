import sys

def findPath(p,m):
    sun = 'COM'
    path = [p]
    k = 0
    while p != sun:
        for x in map:
            if x[1] == p:
                p = x[0]
                path.append(p)
                k = k + 1
                break
    return path

map = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        map.append(line.split(')'))
    
    planets = []
    for list in map:
        for planet in list:
            planets.append(planet)
    planets = set(planets)

    a = findPath('YOU',map)
    b = findPath('SAN',map)

    l1 = 0
    for planet in a:
        if planet in b:
            first_common = planet
            break
        else:
            l1 = l1 + 1
    
    l2 = 0
    for planet in b:
        if planet == first_common:
            break
        else:
            l2 = l2 + 1

    lsum = l1 + l2 - 2
    print(lsum)
