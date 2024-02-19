for i in range(int(input())):
    inp = input().split()
    try:
        print(int(inp[0]) // int(inp[1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
