A, B = [], []
A_count = int(input())
A_elements = set([int(number) for number in input().split()])
B_count = int(input())
B_elements = set([int(number) for number in input().split()])

result = []
for element in A_elements:
    if not element in B_elements and element not in result:
        result.append(element)
for element in B_elements:
    if not element in A_elements and element not in result:
        result.append(element)

for el in sorted(result):
    print(el)