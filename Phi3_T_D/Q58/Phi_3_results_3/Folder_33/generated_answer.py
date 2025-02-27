import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows * cols < 118:
        return 0
    total_sub_matrices = 0
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    sub_matrix_size = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if sub_matrix_size == 118:
                        total_sub_matrices += 1
    return total_sub_matrices