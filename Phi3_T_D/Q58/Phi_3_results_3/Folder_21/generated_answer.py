import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for row_size in range(1, rows - row_start + 1):
                if row_size % (139 // cols) == 0:
                    for col_size in range(1, cols - col_start + 1):
                        if col_size % (139 // row_size) == 0:
                            submatrix = matrix[row_start:row_start + row_size, col_start:col_start + col_size]
                            if submatrix.size == 139:
                                count += 1
    return count