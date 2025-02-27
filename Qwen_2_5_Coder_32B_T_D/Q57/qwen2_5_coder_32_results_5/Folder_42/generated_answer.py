import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(submat):
        return np.sum(submat)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submat = matrix[i:k + 1, j:l + 1]
                    if sum_submatrix(submat) == 862:
                        result.append(submat)
    return result