import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat, r, c):
        submatrices = []
        for i in range(r):
            for j in range(c):
                for p in range(i + 1, r + 1):
                    for q in range(j + 1, c + 1):
                        submatrices.append(mat[i:p, j:q])
        return submatrices
    r, c = matrix.shape
    submatrices = get_submatrices(matrix, r, c)
    result = [submat for submat in submatrices if np.sum(submat) == -394]
    return result