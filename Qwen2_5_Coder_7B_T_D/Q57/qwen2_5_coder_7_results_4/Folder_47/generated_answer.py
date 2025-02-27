import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submatrix):
        return np.sum(submatrix)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix_sum(submatrix) == 27:
                        result.append(submatrix)
    return result