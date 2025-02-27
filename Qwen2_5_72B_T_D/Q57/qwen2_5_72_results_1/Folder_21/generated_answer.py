import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start, end):
        submatrices = []
        for i in range(start, end):
            for j in range(i + 1, end + 2):
                for k in range(matrix.shape[1]):
                    for l in range(k + 1, matrix.shape[1] + 1):
                        submatrix = matrix[i:j, k:l]
                        if np.sum(submatrix) == -936:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices(0, matrix.shape[0] - 1)