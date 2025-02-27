import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 127
    if rows < n or cols < n:
        return 0
    for size_row in range(1, rows - n + 2):
        for size_col in range(1, cols - n + 2):
            for start_row in range(rows - size_row + 1):
                for start_col in range(cols - size_col + 1):
                    submatrix = matrix[start_row:start_row + size_row, start_col:start_col + size_col]
                    if submatrix.size == n:
                        count += 1
    return count