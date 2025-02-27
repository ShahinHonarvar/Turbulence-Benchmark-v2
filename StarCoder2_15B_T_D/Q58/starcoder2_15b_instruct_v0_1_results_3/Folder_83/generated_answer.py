import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    n = 47
    count = 0
    for row in range(num_rows - n + 1):
        for col in range(num_cols - n + 1):
            submatrix = matrix[row:row + n, col:col + n]
            if np.sum(submatrix) == n:
                count += 1
    return count