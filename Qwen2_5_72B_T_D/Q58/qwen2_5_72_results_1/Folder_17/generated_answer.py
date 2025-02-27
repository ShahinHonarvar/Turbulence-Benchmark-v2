import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    target_number = 166
    target_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_number:
                for r in range(i, rows):
                    for c in range(j, cols):
                        if np.sum(matrix[i:r + 1, j:c + 1] == target_number) == target_number:
                            target_count += 1
    return target_count