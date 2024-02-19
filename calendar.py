from calendar import weekday, day_name
inp = input().split()
day = weekday(int(inp[2]), int(inp[0]), int(inp[1]))
day_Name = day_name[day]
print(day_Name.upper())
