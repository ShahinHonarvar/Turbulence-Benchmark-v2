import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(m, n, matrix, size):
        count = 0
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                if np.sum(matrix[i:i + size, j:j + size].flatten() == 37) == 37:
                    count += 1
        return count
    m, n = matrix.shape
    for size in range(min(m, n), 0, -1):
        if size * size == 37:
            return count_submatrices_of_size(m, n, matrix, size)
    return 0