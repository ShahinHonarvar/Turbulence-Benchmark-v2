import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []

    def is_sum_ok(submatrix):
        return np.sum(submatrix) == -128

    def add_submatrix(r1, c1, r2, c2):
        result.append(matrix[r1:r2, c1:c2])
    n = matrix.shape[0]
    for size in range(1, n + 1):
        for r in range(n - size + 1):
            for c in range(n - size + 1):
                if is_sum_ok(matrix[r:r + size, c:c + size]):
                    add_submatrix(r, c, r + size, c + size)
    return result