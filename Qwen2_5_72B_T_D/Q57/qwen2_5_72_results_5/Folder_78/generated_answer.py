import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_17(submatrix):
        return np.sum(submatrix) == 17
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if is_sum_17(submatrix):
                        result.append(submatrix)
    return result