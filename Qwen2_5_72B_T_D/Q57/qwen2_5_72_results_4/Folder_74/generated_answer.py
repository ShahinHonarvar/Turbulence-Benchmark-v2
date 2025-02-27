import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_matrix(mat):
        return np.sum(mat)

    def submatrices(matrix):
        rows, cols = matrix.shape
        for size in range(1, min(rows, cols) + 1):
            for i in range(rows - size + 1):
                for j in range(cols - size + 1):
                    yield matrix[i:i + size, j:j + size]
    result = []
    for sub in submatrices(matrix):
        if sum_matrix(sub) == 88:
            result.append(sub)
    return result