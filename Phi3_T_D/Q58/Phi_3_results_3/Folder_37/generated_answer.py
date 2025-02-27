import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    size = 8
    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            submatrix = matrix[i:i + size, j:j + size]
            if np.all(submatrix == 64):
                count += 1
    return count