import numpy as np

def submatrix_with_n_numbers(matrix):
    if not matrix or not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    for size in range(1, min(rows, cols) + 1):
        for r in range(rows - size + 1):
            for c in range(cols - size + 1):
                submatrix = matrix[r:r + size, c:c + size]
                if submatrix.size == 173:
                    count += 1
    return count