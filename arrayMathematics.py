import numpy

inp = input().split()
N, M = int(inp[0]), int(inp[1])
array_A, array_B = [], []

for i in range(N):
    array_A.append([int(number) for number in input().split()])

for i in range(N):
    array_B.append([int(number) for number in input().split()])

print(numpy.add(numpy.array(array_A), numpy.array(array_B)))
print(numpy.subtract(numpy.array(array_A), numpy.array(array_B)))
print(numpy.multiply(numpy.array(array_A), numpy.array(array_B)))
print(numpy.array(array_A) // numpy.array(array_B))
print(numpy.mod(numpy.array(array_A), numpy.array(array_B)))
print(numpy.power(numpy.array(array_A), numpy.array(array_B)))