from collections import deque

goal = [1,2,3,4,5,6,7,8,0]

def solve(start):
    q = deque([(start, [])])
    v = {tuple(start)}
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        s, p = q.popleft()
        if s == goal:
            return p
        z = s.index(0)
        x, y = divmod(z, 3)
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx*3 + ny
                t = s[:]
                t[z], t[nz] = t[nz], t[z]
                if tuple(t) not in v:
                    v.add(tuple(t))
                    q.append((t, p+[t]))

start = [1,2,3,4,5,6,0,7,8]

for step in solve(start):
    for i in range(0,9,3):
        print(step[i:i+3])
    print()