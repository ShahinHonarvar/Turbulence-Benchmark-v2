import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        n, m = mat.shape
        for size in range(1, min(n, m) + 1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    submatrices.append(mat[i:i + size, j:j + size])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submat for submat in submatrices if np.sum(submat) == 245]
    return result