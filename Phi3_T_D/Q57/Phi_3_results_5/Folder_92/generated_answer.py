import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for k in range(i + 1, len(matrix) + 1):
                    for l in range(j + 1, len(matrix[i]) + 1):
                        yield matrix[i:k, j:l]

    def sum_equals_target(submatrix, target):
        return np.sum(submatrix) == target
    submatrices = [submatrix for submatrix in get_submatrices(matrix) if sum_equals_target(submatrix, -3)]
    return submatrices