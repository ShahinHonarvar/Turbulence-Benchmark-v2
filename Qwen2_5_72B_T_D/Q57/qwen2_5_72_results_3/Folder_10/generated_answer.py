import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(mat):
        n, m = mat.shape
        submatrices = []
        for i in range(n):
            for j in range(m):
                for x in range(i + 1, n + 1):
                    for y in range(j + 1, m + 1):
                        submatrices.append(mat[i:x, j:y])
        return submatrices
    submatrices = all_submatrices(matrix)
    return [submat for submat in submatrices if np.sum(submat) == 56]