import numpy as np

def submatrix_with_n_numbers(matrix):
    count, row, cols = (0, matrix.shape[0], matrix.shape[1])
    n = 23
    for size in range(1, min(row, cols) + 1):
        for i in range(row - size + 1):
            for j in range(cols - size + 1):
                count += 1 if np.count_nonzero(matrix[i:i + size, j:j + size]) == n else 0
    return count