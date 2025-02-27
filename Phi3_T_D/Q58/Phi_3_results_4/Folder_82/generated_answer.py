import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix of integers')
    if matrix.dtype != np.int:
        raise ValueError('Matrix elements must be integers')
    ndim_x, ndim_y = matrix.shape
    count = 0
    for i in range(ndim_x):
        for j in range(ndim_y):
            for k in range(i, ndim_x):
                for l in range(j, ndim_y):
                    submat = matrix[i:k + 1, j:l + 1]
                    if submat.size == 99:
                        count += 1
    return count