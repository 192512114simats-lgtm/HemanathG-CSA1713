tree = [3, 5, 2, 9, 12, 5, 23, 23]

def minimax(d, i, maxi):
    if d == 3:
        return tree[i]
    if maxi:
        return max(minimax(d+1, i*2, False),
                   minimax(d+1, i*2+1, False))
    else:
        return min(minimax(d+1, i*2, True),
                   minimax(d+1, i*2+1, True))

print("Optimal Value:", minimax(0, 0, True))