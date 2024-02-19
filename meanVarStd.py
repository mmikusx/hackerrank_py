import numpy

inp = input().split()
N, M = int(inp[0]), int(inp[1])
rows = []
for i in range(N):
    rows.append([int(number) for number in input().split()])

print(numpy.mean(rows, axis=1))
print(numpy.var(rows, axis=0))
print(round(numpy.std(rows), 11))