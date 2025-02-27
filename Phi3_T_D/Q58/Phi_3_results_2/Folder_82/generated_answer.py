import numpy as np

def submatrix_with_n_numbers(matrix, n=99):
    row_count, col_count = matrix.shape
    count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            for row_len in range(1, row_count - row_start + 1):
                for col_len in range(1, col_count - col_start + 1):
                    submatrix = matrix[row_start:row_start + row_len, col_start:col_start + col_len]
                    if submatrix.size == n:
                        count += 1
    return count