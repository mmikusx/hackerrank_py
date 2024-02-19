import numpy

inp = input().split()
N, M = int(inp[0]), int(inp[1])
rows = []

for i in range(N):
    rows.append([int(number) for number in input().split()])

print(max(numpy.min(rows, axis=1)))