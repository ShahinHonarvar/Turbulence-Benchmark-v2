import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix')
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            if i + 6 >= nrows or j + 6 >= ncols:
                continue
            submatrix = matrix[i:i + 7, j:j + 7]
            if np.all(submatrix == 77):
                count += 1
    return count