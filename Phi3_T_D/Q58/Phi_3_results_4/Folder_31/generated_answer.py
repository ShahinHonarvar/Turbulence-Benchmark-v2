import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return None
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 44 < rows and j + 44 < cols:
                submatrix = matrix[i:i + 45, j:j + 45]
                if submatrix.size == np.count_nonzero(submatrix):
                    count += 1
    return count