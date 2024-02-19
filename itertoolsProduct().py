listA, listB = input(), input()

listA = listA.split(" ")
listB = listB.split(" ")
result = ""

for i in range(len(listA)):
    for j in range(len(listB)):
        result += "(" + listA[i] + ", " + listB[j] + ") "

print(result)