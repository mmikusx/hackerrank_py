import re
ins = []
for i in range(int(input())):
    ins.append(input())

for input in ins:
    try:
        re.compile(input)
        print("True")
    except:
        print("False")