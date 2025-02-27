import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_equal(submat):
        return np.sum(submat) == 8
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submat = matrix[i:k, j:l]
                    if is_sum_equal(submat):
                        result.append(submat)
    return result