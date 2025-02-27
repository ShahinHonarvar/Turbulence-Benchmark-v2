import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_count = 96
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if np.sum((matrix[i:, j:] == matrix[i, j]).astype(int)) == target_count:
                submatrix_count += 1
    return submatrix_count