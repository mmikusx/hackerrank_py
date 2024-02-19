from math import sqrt, atan2

inp = input()
if "+" in inp:
    x, y = int(inp.split("+")[0]), int(inp.split("+")[1][:-1])
elif "-" != inp[:1] and "-" in inp:
    x, y = int(inp.split("-")[0]), inp.split("-")[1][:-1]
    y = int(y) * (-1)
else:
    x, y = inp.split("-")[1], inp.split("-")[2][:-1]
    x = int(x) * (-1)
    y = int(y) * (-1)


r = sqrt(pow(x, 2) + pow(y, 2))
fi = atan2(y, x)

print("{:.3f}".format(r))
print("{:.3f}".format(fi))