a, b = 0, 0

while (a, b) != (2, 3):
    if a == 0:
        a = 4
    elif b == 3:
        b = 0
    else:
        t = min(a, 3 - b)
        a -= t
        b += t
    print((a, b))

print("Goal Reached")