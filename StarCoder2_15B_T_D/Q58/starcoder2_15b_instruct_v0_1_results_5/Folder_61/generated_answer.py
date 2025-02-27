import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 1):
        for j in range(m - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.count_nonzero(submatrix) == 4:
                count += 1
    return count