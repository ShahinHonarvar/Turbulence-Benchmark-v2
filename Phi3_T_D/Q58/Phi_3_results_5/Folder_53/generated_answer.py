import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input should be a numpy matrix')
    nrows, ncols = matrix.shape
    total_count = 0
    target_size = (2, 2)
    for i in range(nrows):
        for j in range(ncols):
            if i + target_size[0] <= nrows and j + target_size[1] <= ncols:
                total_count += 1
    return total_count