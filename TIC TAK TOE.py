b = [[' ']*3 for _ in range(3)]

moves = [
    (0,0,'X'),
    (1,1,'O'),
    (0,1,'X'),
    (1,0,'O'),
    (0,2,'X')
]

def show():
    for i in b:
        print(i)
    print()

def win(p):
    for i in range(3):
        if all(b[i][j]==p for j in range(3)) or all(b[j][i]==p for j in range(3)):
            return True
    return (b[0][0]==b[1][1]==b[2][2]==p or
            b[0][2]==b[1][1]==b[2][0]==p)

for r, c, p in moves:
    b[r][c] = p
    print(p, "moves to", (r, c))
    show()
    if win(p):
        print(p, "Wins!")
        break