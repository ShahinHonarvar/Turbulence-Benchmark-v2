import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                for k in range(i + 1, matrix.shape[0] + 1):
                    for l in range(j + 1, matrix.shape[1] + 1):
                        yield matrix[i:k, j:l]
    result = []
    for submatrix in all_submatrices(matrix):
        if submatrix.sum() == -50:
            result.append(submatrix)
    return result