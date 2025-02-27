import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    valid_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 154:
                        valid_submatrices += 1
    return valid_submatrices