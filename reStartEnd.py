import re

full_string = input()
search_string = input()

res = re.findall(search_string, full_string)
print(res)