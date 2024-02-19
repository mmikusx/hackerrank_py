inp = int(input())

if inp >= 1 and inp <= 10:
    for i in range(inp):
        number = input()
        if len(number) >= 2 and len(number) <= 15 and len(number) == 10 and number[0] in ["7", "8", "9"]:
            isDigit = True
            for i in range(1, len(number)):
                if not number[i].isdigit():
                    isDigit = False
            if isDigit:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")