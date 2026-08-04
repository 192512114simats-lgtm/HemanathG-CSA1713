g = {
    'A':[('B',1),('C',3)],
    'B':[('D',3),('E',6)],
    'C':[('F',5)],
    'D':[],
    'E':[('G',2)],
    'F':[('G',2)],
    'G':[]
}

h = {'A':7,'B':6,'C':4,'D':3,'E':2,'F':1,'G':0}

open = [('A',0)]
path = {'A':None}
cost = {'A':0}

while open:
    open.sort(key=lambda x: x[1] + h[x[0]])
    n, c = open.pop(0)
    if n == 'G':
        break
    for i, w in g[n]:
        nc = c + w
        if i not in cost or nc < cost[i]:
            cost[i] = nc
            path[i] = n
            open.append((i, nc))

p = []
x = 'G'
while x:
    p.append(x)
    x = path[x]

print("Path:", " -> ".join(p[::-1]))
print("Cost:", cost['G'])