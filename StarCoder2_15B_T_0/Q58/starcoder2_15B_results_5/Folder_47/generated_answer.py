import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 90
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix) == n:
                count += 1
    return count