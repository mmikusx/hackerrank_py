from collections import defaultdict

inp = input()
group_A, group_B = int(inp.split()[0]), int(inp.split()[1])
d = defaultdict(list)

i = 1
while i < group_A + 1:
    d['A'].append(input())
    i += 1

i = 1
while i < group_B + 1:
    d['B'].append(input())
    i += 1

for j in range(len(d['B'])):
    result = ""
    for i in range(len(d['A'])):
        if d['B'][j] == (d['A'][i]):
            result += str(i+1) + " "
    if result != "":
        print(result)
    else:
        print("-1")
