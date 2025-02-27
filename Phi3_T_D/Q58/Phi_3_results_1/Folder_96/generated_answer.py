import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix.')
    height, width = matrix.shape
    n = 20 - 1
    count = 0
    for i in range(height):
        for j in range(width):
            if j + n < width and i + n < height:
                count += 1
    return count