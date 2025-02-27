import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.prod(matrix[i:i + size, j:j + size].shape) == 60:
                    count += 1
        return count
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix')
    size = int(np.sqrt(60))
    if size * size != 60:
        raise ValueError('60 cannot be formed by a square submatrix')
    return count_submatrices_of_size(matrix, size)