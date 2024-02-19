from itertools import permutations

def print_permutations(string, size):
    perms = permutations(string, size)

    sorted_perms = sorted(perms)

    for perm in sorted_perms:
        print(''.join(perm))

input_string, size = input().split()
size = int(size)

print_permutations(input_string, size)
