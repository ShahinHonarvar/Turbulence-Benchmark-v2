import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(n, m):
        count = 0
        for i in range(matrix.shape[0] - n + 1):
            for j in range(matrix.shape[1] - m + 1):
                submatrix = matrix[i:i + n, j:j + m]
                if np.prod(submatrix.shape) == 120:
                    count += 1
        return count
    total_count = 0
    for n in range(1, matrix.shape[0] + 1):
        for m in range(1, matrix.shape[1] + 1):
            total_count += count_submatrices(n, m)
    return total_count