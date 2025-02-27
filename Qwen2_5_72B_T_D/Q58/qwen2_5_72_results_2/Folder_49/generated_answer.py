import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m, n, k):
        count = 0
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                if np.prod(matrix[i:i + k, j:j + k].shape) == 72:
                    count += 1
        return count
    m, n = matrix.shape
    k = int(np.sqrt(72))
    if k * k != 72:
        return 0
    return count_submatrices(m, n, k)