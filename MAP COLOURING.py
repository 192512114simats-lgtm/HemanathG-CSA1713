g = [[0,1,1,1],
     [1,0,1,0],
     [1,1,0,1],
     [1,0,1,0]]

n, m = 4, 3
color = [0]*n

def safe(v, c):
    for i in range(n):
        if g[v][i] and color[i] == c:
            return False
    return True

def solve(v):
    if v == n:
        print("Colors:", color)
        return True
    for c in range(1, m+1):
        if safe(v, c):
            color[v] = c
            if solve(v+1): return True
            color[v] = 0

solve(0)
print("1 is red")
print("2 is green")
print("3 is blue")