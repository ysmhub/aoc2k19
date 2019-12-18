# python3 d4p2.py 168630 718098

import sys
from collections import Counter

def hasPairDigits(y):
    found = False
    s = str(y)
    l = len(s)
    for x in range (0,l-1):
        if int(s[x]) == int(s[x+1]):
            found = True
    return found

def neverDecrease(y):
    found = 0
    s = str(y)
    l = len(s)
    for x in range (0,l-1):
        if int(s[x]) <= int(s[x+1]):
            found = found + 1
    
    if found == 5:
        return True
    else:
        return False

def hasLargeGroup(y):
    found = False
    s = str(y)
    l = len(s)
    digits = [int(d) for d in str(y)]
    unique_digits = Counter(digits).keys()
    o = []
    for x in unique_digits:
        start = 0
        count = 0
        for z in range(start,l):
            if int(s[z]) == x:
                count = count + 1
            start = start + 1
        o.append(count)
    
    if 2 in o:
        found = True

    return found

f = 0
if len(sys.argv) == 3:
    password = int(sys.argv[1])
    while password <= int(sys.argv[2]):
        if hasPairDigits(password) and neverDecrease(password):
            if hasLargeGroup(password):
                f = f + 1
        password = password + 1
print (f)
