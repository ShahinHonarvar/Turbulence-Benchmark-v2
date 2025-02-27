import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrices_count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if sub_matrix.size == 18:
                        submatrices_count += 1
    return submatrices_count