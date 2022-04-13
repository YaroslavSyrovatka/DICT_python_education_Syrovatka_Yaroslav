n1, m1 = input('Enter size of first matrix: >').split(" ")
n1 = int(n1)
m1 = int(m1)
matrix1 = []
for i in range(1, n1 + 1):
    ni1 = input('>').split(" ")
    ni1 = list(map(lambda x: int(x), ni1))
    while len(ni1) != m1:
        ni1 = input('>').split(" ")
        ni1 = list(map(lambda x: int(x), ni1))
    matrix1.append(ni1)
n2, m2 = input('Enter size of second matrix: >').split(" ")
n2 = int(n2)
m2 = int(m2)
matrix2 = []
for i in range(1, n2 + 1):
    ni2 = input('>').split(" ")
    ni2 = list(map(lambda x: int(x), ni2))
    while len(ni2) != m2:
        ni2 = input('>').split(" ")
        ni2 = list(map(lambda x: int(x), ni2))
    matrix2.append(ni2)
mix = []
if n1 == n2 and m1 == m2:
    for a1, a2 in zip(matrix1, matrix2):
        column = []
        for a, b in zip(a1, a2):
            value = a + b
            column.append(value)
        mix.append(column)
    print('The result is:')
    for item in mix:
        print(*item, sep=' ')
else:
    print('The operation cannot be performed.')