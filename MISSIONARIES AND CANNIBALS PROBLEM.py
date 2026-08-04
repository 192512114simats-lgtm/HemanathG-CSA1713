from collections import deque

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

q = deque([((3,3,1), [])])
v = {(3,3,1)}
moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

while q:
    (m,c,b), path = q.popleft()
    if (m,c,b) == (0,0,0):
        for s in path + [(m,c,b)]:
            print(s)
        break
    for dm, dc in moves:
        nm, nc = (m-dm, c-dc) if b else (m+dm, c+dc)
        nb = 1 - b
        if valid(nm, nc) and (nm, nc, nb) not in v:
            v.add((nm, nc, nb))
            q.append(((nm, nc, nb), path + [(m,c,b)]))