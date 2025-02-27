import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(i, n_rows):
                for l in range(j, n_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 46:
                        count += 1
    return count