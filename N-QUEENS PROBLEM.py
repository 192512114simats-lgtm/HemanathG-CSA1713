N = 4
b = [[0]*N for _ in range(N)]

def ok(r, c):
    for i in range(r):
        if b[i][c]: return 0
    i, j = r-1, c-1
    while i>=0 and j>=0:
        if b[i][j]: return 0
        i, j = i-1, j-1
    i, j = r-1, c+1
    while i>=0 and j<N:
        if b[i][j]: return 0
        i, j = i-1, j+1
    return 1

def solve(r):
    if r == N:
        for x in b:
            print(x)
        return
    for c in range(N):
        if ok(r, c):
            b[r][c] = 1
            if solve(r+1): return
            b[r][c] = 0

solve(0)