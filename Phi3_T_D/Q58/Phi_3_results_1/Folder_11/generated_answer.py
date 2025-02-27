import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a NumPy matrix')
    n = 38
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(min(rows - i, cols - j), 0, -1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == n:
                    count += 1
    return count