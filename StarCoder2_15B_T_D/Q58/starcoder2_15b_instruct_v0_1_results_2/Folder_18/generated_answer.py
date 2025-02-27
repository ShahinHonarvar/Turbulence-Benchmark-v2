import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 103):
        for j in range(n_cols - 103):
            submatrix = matrix[i:i + 104, j:j + 104]
            if submatrix.size == 104:
                count += 1
    return count