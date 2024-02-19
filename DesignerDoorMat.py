rows, cols = input().split()
rows_len, cols_len = int(rows), int(cols)

pattern = [('.|.' * (2*i + 1)).center(cols_len, '-') for i in range(rows_len//2)]
welcome = 'WELCOME'.center(cols_len, '-')
mat = '\n'.join(pattern + [welcome] + pattern[::-1])

print(mat)