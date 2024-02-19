import numpy

inp = int(input())
array_A, array_B = [], []
for i in range(inp):
    array_A.append([int(number) for number in input().split()])
for i in range(inp):
    array_B.append([int(number) for number in input().split()])

print(numpy.dot(array_A, array_B))