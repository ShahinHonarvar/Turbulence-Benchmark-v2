import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_count = 67
    submatrix_count = 0
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.size(matrix[i:i + size, j:j + size]) == target_count:
                    submatrix_count += 1
    return submatrix_count