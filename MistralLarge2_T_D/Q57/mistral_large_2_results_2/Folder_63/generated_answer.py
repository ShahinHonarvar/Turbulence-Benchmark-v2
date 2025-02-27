import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum):
        n, m = matrix.shape
        submatrices = []
        for i in range(n):
            for j in range(m):
                for k in range(i, n):
                    for l in range(j, m):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices(matrix, 64)