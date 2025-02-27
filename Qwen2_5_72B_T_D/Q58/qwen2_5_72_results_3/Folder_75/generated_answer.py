import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 80
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for row_sub in range(1, rows - i + 1):
                for col_sub in range(1, cols - j + 1):
                    if row_sub * col_sub == target_size:
                        submatrix_count += 1
    return submatrix_count