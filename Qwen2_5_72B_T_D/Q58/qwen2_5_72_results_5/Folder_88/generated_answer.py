import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 67
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if (i + 1) * (j + 1) == n:
                count += np.sum(matrix[:i + 1, :j + 1] == n)
    return count