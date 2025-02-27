import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a two-dimensional numpy matrix.')
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for dr in range(1, rows - r + 1):
                for dc in range(1, cols - c + 1):
                    submatrix = matrix[r:r + dr, c:c + dc]
                    if np.unique(submatrix).size == 2:
                        count += 1
    return count