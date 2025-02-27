import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    target_size = 154
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                if size * size == target_size:
                    submatrix = matrix[i:i + size, j:j + size]
                    count += 1
    return count