import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        for size in range(1, min(rows, cols) + 1):
            for i in range(rows - size + 1):
                for j in range(cols - size + 1):
                    yield mat[i:i + size, j:j + size]
    result = [submatrix for submatrix in get_submatrices(matrix) if np.sum(submatrix) == -38]
    return result