import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 84:
        return 0
    n_rows, n_cols = matrix.shape
    count = 0
    for row in range(n_rows - 2):
        for col in range(n_cols - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if submatrix.size == 84:
                count += 1
    return count