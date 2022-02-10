import numpy as np
from rich import print
from rich.panel import Panel
from rich.text import Text
import random as r


def fancy_print(matrix, op=None, row=None):
    matrix = np.array(matrix)

    buf = Text()

    for i, row_ in enumerate(matrix):
        style = 'white' if i == row else 'green' if sum(row_[:-1]) == 1 and min(row_[:-1]) == 0 and max(
            row_[:-1]) == 1 else 'darkgreen' if np.all(row_ == 0) else 'red1'
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
    for i in range(matrix.shape[1]-1 if matrix.shape[1] <= matrix.shape[0]-1 else matrix.shape[0]):
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
    for i in range(matrix.shape[1]-2 if matrix.shape[1] <= matrix.shape[0]-1 else matrix.shape[0]-1, 0, -1):
        for j in range(i-1, -1, -1):
            m = row_replace(i, j, -1*matrix.item(j, i))
            fancy_print(matrix, m, j)


def solve():
    ref()
    fix()
    rref()
    fix()

def getSolutionMessage():
    # look for pivots in every column except for augmented column
    pivot = np.zeros(0)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix.item(i,j) != 0:
                if j == matrix.shape[1]-1:
                    # No solution if pivot is in the augmented column
                    return "No Solution"
                pivot = np.append(pivot, j)
                break
    for i in range(matrix.shape[1]-1):
        if not np.isin(i, pivot):
            # Many solutions if any row doesn't have a pivot
            return "Infinitely Many Solutions"
    # Unique solution if each non-augmented column has a pivot
    return "Unique Solution"

def generateRandomMatrix():
    matrix = np.zeros((r.randint(minrows,maxrows), r.randint(maxrows,maxcolumns)),dtype=np.float64)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix.itemset((i,j), r.randint(-10,10))
    return matrix

def fix():
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if abs(matrix.item(i,j)-1) <= errormargin:
                matrix.itemset((i,j), 1)
            if abs(matrix.item(i,j)) <= errormargin:
                matrix.itemset((i,j), 0)

# var = int(input("How many variables?"))
# equ = int(input("How many equations?"))
var = 3
equ = 3

errormargin = 0.000001

# matrix = np.zeros((equ, var+1))
#
# for i in range(equ):
#     val = np.matrix(input("Please input first equation's coefficents"), dtype=np.float64)
#     matrix[i] = val

# Generate random matrix
maxcolumns = 10
mincolumns = 6
maxrows = 10
minrows = 5

# matrix = np.zeros((r.randint(1,maxrows), r.randint(2,maxcolumns)),dtype=np.float64)
# for i in range(matrix.shape[0]):
#     for j in range(matrix.shape[1]):
#         matrix.itemset((i,j), r.randint(-10,10))
#
# matrix = np.mat([[1, -1, -5, -3,   5, 4],
#                  [2,  0, 4,   0,   0, 3],
#                  [1,  0, 1,   5,   0, 2],
#                  [1,  3, 0,   0,  9, 1],
#                  [2,  3, 1,   0,  7, 1]],
#                 dtype=np.float64)

matrix = np.mat([[1, 1, 2, -1, 0],
                 [1,  0, 1,   1, 0],
                 [0,  1, 0,   1, 0],
                 [-1,  1, 1,   0, 0]],
                dtype=np.float64)

for i in range(1):
    # matrix = generateRandomMatrix()

    fancy_print(matrix)

    solve()



    fancy_print(matrix, getSolutionMessage())
