import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy matrix.')
    height, width = matrix.shape
    count = 0
    for size in range(1, min(height, width) + 1):
        for i in range(height - size + 1):
            for j in range(width - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 180:
                    count += 1
    return count