import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix.')
    if matrix.ndim != 2:
        raise ValueError('Matrix must be two-dimensional.')

    def count_submatrices(m, n, count):
        if m == 0 or n == 0:
            return count
        for i in range(0, matrix.shape[0] - m + 1):
            for j in range(0, matrix.shape[1] - n + 1):
                yield matrix[i:i + m, j:j + n]
    count_49 = sum((1 for submatrix in count_submatrices(3, 3, 0) if submatrix.size == 49))
    return count_49