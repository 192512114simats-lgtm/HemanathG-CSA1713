tree = [3, 5, 2, 9, 12, 5, 23, 23]

def alphabeta(d, i, maxi, a, b):
    if d == 3:
        return tree[i]

    if maxi:
        v = -999
        for k in [0, 1]:
            v = max(v, alphabeta(d+1, i*2+k, False, a, b))
            a = max(a, v)
            if a >= b:
                break
        return v
    else:
        v = 999
        for k in [0, 1]:
            v = min(v, alphabeta(d+1, i*2+k, True, a, b))
            b = min(b, v)
            if a >= b:
                break
        return v

print("Optimal Value:", alphabeta(0, 0, True, -999, 999))