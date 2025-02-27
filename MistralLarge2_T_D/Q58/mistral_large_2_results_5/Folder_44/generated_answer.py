import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def count_submatrices(matrix, start_row, end_row, start_col, end_col):
        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
        if submatrix.size == 191:
            return 1
        return 0
    for start_row in range(rows):
        for end_row in range(start_row, rows):
            for start_col in range(cols):
                for end_col in range(start_col, cols):
                    count += count_submatrices(matrix, start_row, end_row, start_col, end_col)
    return count