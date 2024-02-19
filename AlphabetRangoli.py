def print_rangoli(size):
    import string
    lines = []

    for i in range(size):
        s = "-".join(string.ascii_lowercase[i:size])
        lines.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))

    print("\n".join(lines[:0:-1] + lines))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)