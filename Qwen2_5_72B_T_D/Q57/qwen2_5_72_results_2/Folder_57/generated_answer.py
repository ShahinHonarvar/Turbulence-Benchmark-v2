import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, r, c):
        for size in range(1, min(r, c) + 1):
            for i in range(r - size + 1):
                for j in range(c - size + 1):
                    yield matrix[i:i + size, j:j + size]
    r, c = matrix.shape
    result = []
    for sub in submatrices(matrix, r, c):
        if np.sum(sub) == 13:
            result.append(sub)
    return result