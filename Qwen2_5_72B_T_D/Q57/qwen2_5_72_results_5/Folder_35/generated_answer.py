import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, r, c):
        for i in range(r):
            for j in range(c):
                for p in range(i + 1, r + 1):
                    for q in range(j + 1, c + 1):
                        yield matrix[i:p, j:q]
    r, c = matrix.shape
    result = []
    for sub in submatrices(matrix, r, c):
        if np.sum(sub) == 432:
            result.append(sub)
    return result