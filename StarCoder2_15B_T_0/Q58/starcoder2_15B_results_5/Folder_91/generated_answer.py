import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 4):
        for j in range(n_cols - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if submatrix.size == 5:
                count += 1
    return count