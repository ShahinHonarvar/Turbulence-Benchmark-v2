import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    results = []

    def check_sum(submatrix):
        return np.sum(submatrix) == 95
    for size in range(1, min(m, n) + 1):
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if check_sum(submatrix):
                    results.append(submatrix)
    return results