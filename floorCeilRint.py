import numpy
numpy.set_printoptions(legacy='1.13')

rows = []
rows.append([float(number) for number in input().split()])

print(numpy.floor(numpy.array(rows))[0])
print(numpy.ceil(numpy.array(rows))[0])
print(numpy.rint(numpy.array(rows))[0])