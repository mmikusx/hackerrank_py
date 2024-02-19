import numpy

inp = [float(number) for number in input().split()]
x = float(input())

print(numpy.polyval(inp, x))