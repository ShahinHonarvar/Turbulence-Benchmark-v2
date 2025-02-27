import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.size == 0 or 176 > min(matrix.shape) * min(matrix.shape):
        return 0
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 13):
        for j in range(cols - 13):
            if matrix[i:i + 13, j:j + 13].size == 176:
                count += 1
    return count