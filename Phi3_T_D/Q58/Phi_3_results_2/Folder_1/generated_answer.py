import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for sub_matrix_size in range(2, min(rows - row_start + 1, cols - col_start + 1)):
                if sub_matrix_size * (sub_matrix_size + 1) // 2 == 23:
                    count += 1
                else:
                    break
    return count