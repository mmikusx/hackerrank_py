import numpy

array_A = [int(number) for number in input().split()]
array_B = [int(number) for number in input().split()]

print(numpy.inner(array_A, array_B))
print(numpy.outer(array_A, array_B))