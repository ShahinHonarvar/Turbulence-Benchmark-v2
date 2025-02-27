import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    rows, cols = matrix.shape
    n = 80
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.count_nonzero(matrix[i:i + size, j:j + size]) >= n:
                    count += 1
    return count