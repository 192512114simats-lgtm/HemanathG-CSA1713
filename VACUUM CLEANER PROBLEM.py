rooms = {'A': 1, 'B': 0}   
pos = 'A'

for r in ['A', 'B']:
    pos = r
    print("Vacuum is at", pos)
    if rooms[pos]:
        print("Cleaning room", pos)
        rooms[pos] = 0

print("Final State:", rooms)