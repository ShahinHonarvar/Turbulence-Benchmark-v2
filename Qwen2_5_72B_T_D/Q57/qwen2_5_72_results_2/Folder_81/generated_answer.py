import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        R, C = mat.shape
        for i in range(R):
            for j in range(C):
                for p in range(i + 1, R + 1):
                    for q in range(j + 1, C + 1):
                        yield mat[i:p, j:q]
    result = []
    for sub in get_submatrices(matrix):
        if np.sum(sub) == -90:
            result.append(sub)
    return result