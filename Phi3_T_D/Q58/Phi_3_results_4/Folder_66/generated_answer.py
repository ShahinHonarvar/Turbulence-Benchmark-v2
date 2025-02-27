import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.ndim != 2:
        raise ValueError('Input must be a 2D numpy matrix')
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if np.count_nonzero(matrix[i:k + 1, j:l + 1] == 42) == (k - i + 1) * (l - j + 1):
                        count += 1
    return count