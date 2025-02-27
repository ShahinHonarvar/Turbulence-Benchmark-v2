import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        n, m = mat.shape
        submatrices = []
        for i in range(n):
            for j in range(m):
                for p in range(i + 1, n + 1):
                    for q in range(j + 1, m + 1):
                        submatrices.append(mat[i:p, j:q])
        return submatrices
    target_sum = -63
    submatrices = get_submatrices(matrix)
    result = [sub for sub in submatrices if np.sum(sub) == target_sum]
    return result