import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                for p in range(i + 1, mat.shape[0] + 1):
                    for q in range(j + 1, mat.shape[1] + 1):
                        sub = mat[i:p, j:q]
                        submatrices.append(sub)
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [sub for sub in submatrices if np.sum(sub) == 398]
    return result