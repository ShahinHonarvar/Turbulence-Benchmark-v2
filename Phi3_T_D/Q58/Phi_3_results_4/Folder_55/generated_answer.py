import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')

    def num_submatrices_with_n_integers(submatrix, n):
        count = 0
        for i in range(submatrix.shape[0] - n + 1):
            for j in range(submatrix.shape[1] - n + 1):
                if np.sum(submatrix[i:i + n, j:j + n]) == n * (submatrix[0, 0] + 1) * n:
                    count += 1
        return count
    count = 0
    for size in range(1, min(matrix.shape[0], matrix.shape[1]) + 1):
        if size == 39:
            continue
        count += num_submatrices_with_n_integers(matrix, size)
    return count