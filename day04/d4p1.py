# python3 d4p1.py 168630 718098

import sys

def has_same_adjacent_digits(y):
    found = False
    s = str(y)
    l = len(s)
    for x in range (0,l-1):
        if s[x] == s[x+1]:
            found = True
    return found

def is_never_decrease(y):
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

f = 0
if len(sys.argv) == 3:
    password = int(sys.argv[1])
    while password <= int(sys.argv[2]):
        if has_same_adjacent_digits(password) and is_never_decrease(password):
            f = f + 1
        password = password + 1
print (f)
