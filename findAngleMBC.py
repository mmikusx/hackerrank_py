from math import sqrt, asin, degrees

AB = int(input())
BC = int(input())

AC = sqrt(pow(AB, 2) + pow(BC, 2))

halfAC = AC / 2

degreeMBC = degrees(asin(halfAC / BC))
if degreeMBC - int(degreeMBC) >= 0.5:
    print(str(int(degreeMBC + 1)) + "°")
else:
    print(str(int(degreeMBC)) + "°")
