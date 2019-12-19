import sys
import pandas as pd

with open(sys.argv[1]) as f:
    df = pd.read_csv(f,sep=')',header=None)
    planets = set(list(df[0]) + list(df[1]))
    
    tk = 0
    for planet in planets:
        sun = 'COM'
        path = planet
        k = 0
        while planet != sun:
            for x in range(0,len(df)):
                if df.loc[x,1] == planet:
                    planet = df.loc[x,0]
                    path += f"-{planet}"
                    k = k + 1
                    break
        print (f"{path},({k})")
        tk = tk + k
    print(f"total number of direct and indirect orbits: {tk}")



