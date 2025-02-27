import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input needs to be a numpy matrix')
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            for size in range(1, min(rows - i, columns - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 33:
                    count += 1
    return count