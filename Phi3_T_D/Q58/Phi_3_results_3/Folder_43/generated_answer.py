import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('The input must be a numpy array.')
    if matrix.ndim != 2 or not matrix.dtype.kind in 'iufb':
        raise ValueError('The input must be a two-dimensional matrix of integers.')
    rows, cols = matrix.shape
    count = 0
    for x in range(rows):
        for y in range(cols):
            if x + 2 < rows and y + 2 < cols:
                submatrix = matrix[x:x + 3, y:y + 3]
                if submatrix.size == 85:
                    count += 1
    return count