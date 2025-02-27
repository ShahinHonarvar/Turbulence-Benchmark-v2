import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 107 + 1):
        for j in range(n_cols - 107 + 1):
            submatrix = matrix[i:i + 107, j:j + 107]
            if submatrix.size == 107:
                count += 1
    return count