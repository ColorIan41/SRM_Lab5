import numpy as np
from copy import deepcopy


def truth_table(var, f):
    table = deepcopy(var)
    for i in range(0, len(f)):
        table[i].append(f[i])
    table = np.array(table)
    return table


def dual(f):
    dualfunc = deepcopy(f)
    for i in range(0, int(len(f) / 2)):
        if f[len(f) - i - 1] == f[i]:
            if f[i] == 0:
                dualfunc[len(f) - 1 - i] = 1
            else:
                dualfunc[len(f) - 1 - i] = 0
    return dualfunc


def check_func(table, f):
    const_zero = False
    for i in table:
        if np.isin(table[i], [0]).all():
            const_zero = True

    const_one = False
    for i in table:
        if np.isin(table[i], [1]).all():
            const_one = True

    is_dual = True
    for i in range(0, int(len(f) / 2)):
        if f[i] == f[int(len(f) - 1 - i)]:
            is_dual = False

    is_monotone = True
    for i in range(0, (len(f) - 1)):
        if f[i] > f[i + 1]:
            is_monotone = False

    is_linear = True
    for i in range(0, len(f)):
        if table[i][0] and table[i][1] and table[i][2] != f[i]:
            is_linear = False
        elif table[i][0] or table[i][1] or table[i][2] != f[i]:
            is_linear = False
    print("\nЗберігає константу 0: ", const_zero,
          '\nЗберігає константу 1: ', const_one,
          '\nCамодвоїста: ', is_dual,
          "\nМонотонна: ", is_monotone,
          "\nЛінійна: ", is_linear)

def pdnf(table):
    output = "F = "
    for i in range(0, len(table) - 1):
        if table[i][3] == 1:
            output += '('
            for j in range(0, 3):  # ¬
                if j == 0:
                    var = 'X'
                elif j == 1:
                    var = 'Y'
                else:
                    var = 'Z'
                if table[i][j] == 0:
                    output += '¬' + var + ' ∧ '
                else:
                    output += var + ' ∧ '
            output = output[0: -3]
            output += ") v "
    return output[0:-3]


def pcnf(table):
    output = "F = "
    for i in range(0, len(table) - 1):
        if table[i][3] == 0:
            output += '('
            for j in range(0, 3):  # ¬
                if j == 0:
                    var = 'X'
                elif j == 1:
                    var = 'Y'
                else:
                    var = 'Z'
                if table[i][j] == 1:
                    output += '¬' + var + ' v '
                else:
                    output += var + ' v '
            output = output[0: -3]
            output += ") ∧ "
    return output[0: -3]


def zhegalkin(table, f):
    items = f
    triangle = []
    tempResult = []
    for i in range(0, len(items)):
        tempResult.append(items[0])
        for item in range(0, (len(items) - 1)):
            temp = items[item] ^ items[item + 1]
            triangle.append(temp)
        items = triangle
        triangle = []

    output = 'F3 = '
    for i in range(0, len(tempResult)):
        if tempResult[i] != 0:
            for j in range(0, 4):
                if j == 0 and table[i][j] != 0:
                    output += 'X'
                elif j == 1 and table[i][j] != 0:
                    output += 'Y'
                elif j == 2 and table[i][j] != 0:
                    output += 'Z'
                elif j == 3 and i == 0 and table[i][j] != 0:
                    output += '1'
            output += ' ⊕ '
    return output[0:-2]


def print_info(table, f):
    print("Таблиця істинності:")
    print("  x y z F")
    print(str(table))
    check_func(table, f)
    print("\nДДНФ:\n", pdnf(table))
    print("\nДКНФ:\n", pcnf(table))
    print("\nПоліном Жегалкіна:\n", zhegalkin(table, f))
