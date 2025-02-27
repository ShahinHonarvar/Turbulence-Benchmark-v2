import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            if row_start + 7 <= row_count and col_start + 6 <= col_count:
                submatrix = matrix[row_start:row_start + 7, col_start:col_start + 6]
                flattened_submatrix = submatrix.flatten()
                if flattened_submatrix.size == 4 * 3 == 18:
                    count += 1
    return count