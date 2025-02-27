import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for row_length in range(1, rows - row_start + 1):
                for col_length in range(1, cols - col_start + 1):
                    if row_length * col_length == 16:
                        submat = matrix[row_start:row_start + row_length, col_start:col_start + col_length]
                        if submat.size == 16:
                            count += 1
    return count