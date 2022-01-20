import numpy as np

def row_multiply(row, factor):
    matrix[row] = matrix[row]*factor

def row_swap(row1, row2):
    temp = np.copy(matrix[row1])
    matrix[row1] = matrix[row2]
    matrix[row2] = temp

def row_replace(row1, row2, factor):
    temp = np.copy(matrix[row1]*factor)
    matrix[row2] = matrix[row2] + temp

def solve():
    ref()

def ref():
    for i in range(matrix.shape[1]-1):
        if matrix.item(i,i) == 0:
            row_swap(i,i+1)
            i-=1
            print(matrix)
            continue
        else:
            row_multiply(i,1/matrix.item(i,i))
        print(matrix)
        for j in range(i+1,matrix.shape[0]):
            row_replace(i,j,-1*matrix.item(j,i))
            print(matrix)

# var = int(input("How many variables?"))
# equ = int(input("How many equations?"))
var = 3
equ = 3

# matrix = np.zeros((equ, var+1))
#
# for i in range(equ):
#     val = np.matrix(input("Please input first equation's coefficents"))
#     matrix[i] = val

matrix = np.mat([[1., 2., 3., 6.],
        [1., 3., 5., 4.],
        [3., 2., 3., 4.]])

print(matrix)

solve()

print(matrix)
