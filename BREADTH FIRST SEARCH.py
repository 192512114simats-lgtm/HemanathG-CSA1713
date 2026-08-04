from collections import deque

g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

q = deque(['A'])
v = {'A'}

while q:
    n = q.popleft()
    print(n, end=" ")
    for i in g[n]:
        if i not in v:
            v.add(i)
            q.append(i)