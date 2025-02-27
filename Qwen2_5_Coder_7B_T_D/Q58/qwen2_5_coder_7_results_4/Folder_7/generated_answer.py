import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if k - i == 1 and l - j == 1:
                        if matrix[i, j] == 1 and matrix[i, l] == 2 and (matrix[k, j] == 1) and (matrix[k, l] == 1):
                            count += 1
    return count