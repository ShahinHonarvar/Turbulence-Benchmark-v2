import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input should be a two-dimensional numpy matrix')
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 73 >= rows or j + 73 >= cols:
                continue
            submatrix = matrix[i:i + 74, j:j + 74]
            if np.sum(submatrix == 74) == 74:
                count += 1
    return count