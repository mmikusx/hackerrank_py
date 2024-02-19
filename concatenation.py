import numpy

N, M, P = map(int, input().split())

rows = []
for i in range(N):
    rows.append(list(map(int, input().split())))

for i in range(M):
    rows.append(list(map(int, input().split())))

print(numpy.array(rows))
# print(numpy.concatenate(list(rows)))