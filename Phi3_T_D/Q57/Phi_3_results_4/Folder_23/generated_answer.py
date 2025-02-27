import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        submatrices.append(matrix[i:k + 1, j:l + 1])
        return submatrices

    def has_sum_of_59(submatrix):
        return np.sum(submatrix) == 59
    submatrices = get_submatrices(matrix)
    desired_submatrices = [submatrix for submatrix in submatrices if has_sum_of_59(submatrix)]
    return desired_submatrices