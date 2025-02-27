import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_valid_submatrix(submatrix):
        return np.sum(submatrix) == 34
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if is_valid_submatrix(submatrix):
                        submatrices.append(submatrix)
    return submatrices