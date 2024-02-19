import numpy

inp = int(input())
rows = []
for i in range(inp):
    rows.append([float(row) for row in input().split()])

print(round(numpy.linalg.det(rows), 2))