import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(m, n):
        for size in range(1, min(m, n) + 1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    yield matrix[i:i + size, j:j + size]
    submatrices = generate_submatrices(matrix.shape[0], matrix.shape[1])
    result = [sub for sub in submatrices if np.sum(sub) == 69]
    return result