def print_formatted(number):
    max_width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal.rjust(max_width)} {octal.rjust(max_width)} {hexa.rjust(max_width)} {binary.rjust(max_width)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)