def multiply_table():
    table = []
    for i in range(256):
        row = []
        for j in range(256):
            result = i * j
            row.append(result)
        table.append(row)
    return table

def print_table(table):
    print('      |', end='')
    for i in range(256):
        print(f' {format(i, "02X")}', end='')
    print('\n' + '-' * 104)
    for i in range(256):
        print(f'{format(i, "02X")}    |', end='')
        for j in range(256):
            print(f' {table[i][j]:04X}', end='')
        print()

# Generate and print the multiplication table
table = multiply_table()
print_table(table)