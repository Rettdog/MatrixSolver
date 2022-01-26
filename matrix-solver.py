import numpy as np
from rich import print
from rich.panel import Panel
from rich.text import Text


def fancy_print(matrix, op=None, row=None):
    matrix = np.array(matrix)

    buf = Text()

    for i, row_ in enumerate(matrix):
        style = 'yellow' if i == row else 'green' if sum(row_[:-1]) == 1 and min(row_[:-1]) == 0 and max(
            row_[:-1]) == 1 else 'red'
        buf.append(''.join((
            f'{item:8.2f}'
            for item in row_
        ))+'\n', style=style)

    p = Panel(buf, title=op, expand=False, padding=2)

    print(p)


def row_multiply(row, factor):
    matrix[row] = matrix[row]*factor

    # explanation of row multiplication
    return f'R{row+1} -> R{row+1} * {factor:.2f}'


def row_swap(row1, row2):
    temp = np.copy(matrix[row1])
    matrix[row1] = matrix[row2]
    matrix[row2] = temp

    # explanation of row swap
    return f'R{row1+1} <-> R{row2+1}'


def row_replace(row1, row2, factor):
    temp = np.copy(matrix[row1]*factor)
    matrix[row2] += temp

    # explanation of row replacement
    return f'R{row2+1} -> R{row2+1} + R{row1+1} * {factor:.2f}'


def ref():
    for i in range(matrix.shape[1]-1):
        if matrix.item(i, i) == 0:
            for j in range(matrix.shape[0]-1,i,-1):
                if matrix.item(j,i) != 0:
                    m = row_swap(i,j)
                    fancy_print(matrix, m, j)

                    m= row_multiply(i, 1/matrix.item(i,i))
                    fancy_print(matrix, m, i)
                    break
            # i-=1
            # continue
        else:
            m = row_multiply(i, 1/matrix.item(i, i))
        fancy_print(matrix, m, i)
        for j in range(i+1, matrix.shape[0]):
            m = row_replace(i, j, -1*matrix.item(j, i))
            fancy_print(matrix, m, j)


def rref():
    for i in range(matrix.shape[1]-2, 0, -1):
        for j in range(i-1, -1, -1):
            m = row_replace(i, j, -1*matrix.item(j, i))
            fancy_print(matrix, m, j)


def solve():
    ref()
    rref()

def getSolutionMessage():
    for i in range(matrix.shape[0]):
        if np.all(matrix[i,:-1] == 0):
            if matrix[i,-1] != 0:
                return "No Solution"
            else:
                return "Infinitely Many Solutions"
    return "Unique Solution"



# var = int(input("How many variables?"))
# equ = int(input("How many equations?"))
var = 3
equ = 3

# matrix = np.zeros((equ, var+1))
#
# for i in range(equ):
#     val = np.matrix(input("Please input first equation's coefficents"), dtype=np.float64)
#     matrix[i] = val

matrix = np.mat([[1, -1, -5, -3],
                 [2,  0, 4,  1],
                 [1,  0, 1.5,  0.5]],
                dtype=np.float64)

fancy_print(matrix)

solve()

fancy_print(matrix, getSolutionMessage())
