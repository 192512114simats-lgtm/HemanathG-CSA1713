g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

v = set()

def dfs(n):
    if n not in v:
        print(n, end=" ")
        v.add(n)
        for i in g[n]:
            dfs(i)

dfs('A')