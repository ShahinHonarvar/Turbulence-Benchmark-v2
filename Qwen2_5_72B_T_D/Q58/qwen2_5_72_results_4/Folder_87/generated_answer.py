import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    count = 0
    target_elements = 96
    for i in range(matrix.shape[0] - 9 + 1):
        for j in range(matrix.shape[1] - 10 + 1):
            submatrix = matrix[i:i + 9, j:j + 10]
            if submatrix.size == target_elements:
                count += 1
    return count