import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 17
    rows, cols = matrix.shape
    count = 0
    for row_top in range(rows):
        for col_left in range(cols):
            for sub_row_len in range(1, rows - row_top + 1):
                sub_col_len = min(n // sub_row_len, cols - col_left)
                sub_matrix = matrix[row_top:row_top + sub_row_len, col_left:col_left + sub_col_len]
                if sub_matrix.size == n:
                    count += 1 if (sub_matrix == matrix).all() else 0
    return count