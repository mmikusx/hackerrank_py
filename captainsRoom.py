inp = int(input())
rooms = map(int, input().split())
counts = {}
for room in rooms:
    counts[room] = counts.get(room, 0) + 1

for key, val in counts.items():
    if val != inp:
        print(key)
