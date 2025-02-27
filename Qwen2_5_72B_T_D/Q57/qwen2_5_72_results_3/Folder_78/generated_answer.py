import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(mat):
        m, n = mat.shape
        submatrices = []
        for i in range(m):
            for j in range(n):
                for p in range(i + 1, m + 1):
                    for q in range(j + 1, n + 1):
                        submatrices.append(mat[i:p, j:q])
        return submatrices
    submatrices = get_all_submatrices(matrix)
    result = [submat for submat in submatrices if np.sum(submat) == 17]
    return result