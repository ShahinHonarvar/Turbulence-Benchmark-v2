import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    target_size = 180
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            for h in range(1, rows - i + 1):
                for w in range(1, cols - j + 1):
                    if h * w == target_size:
                        submatrix_count += 1
    return submatrix_count