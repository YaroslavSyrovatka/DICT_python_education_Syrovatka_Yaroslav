def sum_matrix():
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


def constanta_matrix():
    n1, m1 = input('Enter size of matrix: >').split(" ")
    n1 = int(n1)
    m1 = int(m1)
    matrix1 = []
    for i in range(1, n1 + 1):
        ni1 = input('>').split(" ")
        ni1 = list(map(lambda x: float(x), ni1))
        while len(ni1) != m1:
            ni1 = input('>').split(" ")
            ni1 = list(map(lambda x: float(x), ni1))
        matrix1.append(ni1)
    const = float(input('Enter constant: >'))
    mix = []
    for rows in matrix1:
        items = []
        for item in rows:
            items.append(item * const)
        mix.append(items)
    print('The result is:')
    for item in mix:
        print(*item, sep=' ')


def multiply_matrix():
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
    if m1 == n2:
        mix = []
        for i in range(n1):
            row = []
            for j in range(m2):
                num = 0
                for k in range(m1):
                    num += matrix1[i][k] * matrix2[k][j]
                row.append(num)
            mix.append(row)
        print('The result is:')
        for item in mix:
            print(*item, sep=' ')
    else:
        print('The operation cannot be performed.')


def trans_matrix():
    try:
        print('''1. Main diagonal
    2. Side diagonal
    3. Vertical line
    4. Horizontal line''')
        choise = int(input('Your choice: >'))
        n1, m1 = input('Enter matrix size: >').split(" ")
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
        mix = []
        if choise == 1:
            for i in range(len(matrix1[0])):
                rows = []
                for row in matrix1:
                    rows.append(row[i])
                mix.append(rows)
            print('The result is:')
            for item in mix:
                print(*item, sep=' ')
        elif choise == 2:
            for i in range(len(matrix1[0])):
                rows = []
                for row in matrix1:
                    rows.append(row[i])
                mix.append(rows)
                mix.reverse()
                rows.reverse()
            print('The result is:')
            for item in mix:
                print(*item, sep=' ')
        elif choise == 3:
            for rows in matrix1:
                rows.reverse()
            print('The result is:')
            for item in matrix1:
                print(*item, sep=' ')
        elif choise == 4:
            matrix1.reverse()
            print('The result is:')
            for item in matrix1:
                print(*item, sep=' ')
    except ValueError:
        trans_matrix()


def menu():
    try:
        print('''1.Add matrices
2.Multiply matrix by a constant
3.Multiply matrices
4.Transpose matrix
5.Calculate a determinant
6.Inverse matrix
0.Exit''')
        choise = int(input('Your choice: >'))
        if choise == 1:
            sum_matrix()
            menu()
        elif choise == 2:
            constanta_matrix()
            menu()
        elif choise == 3:
            multiply_matrix()
            menu()
        elif choise == 4:
            trans_matrix()
            menu()
        # elif choise == 5:
        #     determinate_matrix()
        #     menu()
        # elif choise == 6:
        #     invers()
        #     menu()
        elif choise == 0:
            exit()
        else:
            menu()
    except ValueError:
        menu()


menu()

