import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or matrix.dtype != int:
        raise ValueError('Input must be a two-dimensional numpy matrix of integers.')

    def count_in_submatrix(start_r, start_c, end_r, end_c):
        return np.sum(np.sum(matrix[start_r:end_r + 1, start_c:end_c + 1]))
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if count_in_submatrix(i, j, k, l) == 173:
                        count += 1
    return count