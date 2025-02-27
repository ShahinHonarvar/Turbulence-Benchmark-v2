import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(m, n):
        for i in range(m):
            for j in range(n):
                for p in range(i + 1, m + 1):
                    for q in range(j + 1, n + 1):
                        yield matrix[i:p, j:q]
    result = [submatrix for submatrix in submatrices(matrix.shape[0], matrix.shape[1]) if np.sum(submatrix) == -36]
    return result