import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(m):
        submatrices = []
        rows, cols = m.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        sub = m[i:k + 1, j:l + 1]
                        submatrices.append(sub)
        return submatrices
    result = []
    submatrices = get_submatrices(matrix)
    for sub in submatrices:
        if np.sum(sub) == -811:
            result.append(sub)
    return result