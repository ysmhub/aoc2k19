import sys

map = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        map.append(line.split(')'))
    
    print(map)
    
    planets = []
    for list in map:
        for planet in list:
            planets.append(planet)

    planets = set(planets)
    print(set(planets))
    
    tk = 0
    for planet in planets:
        sun = 'COM'
        path = planet
        k = 0
        while planet != sun:
            for x in map:
                if x[1] == planet:
                    planet = x[0]
                    path += f"-{planet}"
                    k = k + 1
                    break
        print (f"{path},({k})")
        tk = tk + k
    print(f"total number of direct and indirect orbits: {tk}")
