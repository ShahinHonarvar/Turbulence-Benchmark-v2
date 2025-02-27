import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    target_elements = 24
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 4 <= rows and j + 6 <= cols:
                if np.size(matrix[i:i + 4, j:j + 6]) == target_elements:
                    count += 1
    return count