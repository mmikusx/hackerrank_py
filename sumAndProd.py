import numpy

inp = input().split()
N, M = int(inp[0]), int(inp[1])
rows = []

for i in range(N):
    rows.append([int(number) for number in input().split()])

print(numpy.prod(numpy.sum(rows, axis=0), axis=None))