import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if k - i == 2 and l - j == 2 and (matrix[i][j] == 1) and (matrix[i][l] == 3) and (matrix[k][j] == 1) and (matrix[k][l] == 1):
                        count += 1
    return count