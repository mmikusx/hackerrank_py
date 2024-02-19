from collections import namedtuple

inp = int(input())
Table = namedtuple('Table', input().split())
total_mark = 0
for i in range(inp):
    pt = Table(*input().split())
    total_mark += float(pt.MARKS)

print("{:.2f}".format(total_mark / inp))