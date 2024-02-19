x, k = map(int, input().split())
f = input()
res = eval(f.replace("x", f'{x}'))

if res == k:
    print("True")
else:
    print("False")