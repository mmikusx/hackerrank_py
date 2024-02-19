from collections import Counter

number_of_shoes = int(input())
shoe_sizes = [int(size) for size in input().split()]
number_of_customers = int(input())
total_earned = 0
i = 1
while i < number_of_customers + 1:
    inp = input()
    shoe_size = int(inp.split()[0])
    shoe_price = int(inp.split()[1])
    if shoe_size in list(Counter(shoe_sizes).keys()):
        shoe_sizes.pop(shoe_sizes.index(shoe_size))
        total_earned += shoe_price
    i += 1

print(total_earned)