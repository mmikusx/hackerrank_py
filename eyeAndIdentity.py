import numpy
numpy.set_printoptions(legacy='1.13')

inp = input().split()
N, M = int(inp[0]), int(inp[1])
rows = []

if N == M:
    print(numpy.identity(N))
else:
    print(numpy.eye(N,M,k=0))