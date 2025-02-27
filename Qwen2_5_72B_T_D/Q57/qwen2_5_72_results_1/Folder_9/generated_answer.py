import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        n, m = matrix.shape
        submatrices = []
        for i in range(n):
            for j in range(m):
                for i_end in range(i + 1, n + 1):
                    for j_end in range(j + 1, m + 1):
                        submatrix = matrix[i:i_end, j:j_end]
                        submatrices.append(submatrix)
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == -86]
    return result