import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                for p in range(i + 1, rows + 1):
                    for q in range(j + 1, cols + 1):
                        yield mat[i:p, j:q]
    result = []
    for submatrix in get_submatrices(matrix):
        if np.sum(submatrix) == -811:
            result.append(submatrix)
    return result