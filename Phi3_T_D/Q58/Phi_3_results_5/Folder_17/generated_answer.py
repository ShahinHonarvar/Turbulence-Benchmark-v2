import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a 2D NumPy matrix')
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 3 < rows and j + 3 < cols:
                submatrix = matrix[i:i + 4, j:j + 4]
                if np.sum(submatrix) == 166:
                    count += 1
    return count