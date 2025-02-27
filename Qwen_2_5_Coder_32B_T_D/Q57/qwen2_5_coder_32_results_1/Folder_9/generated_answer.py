import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(submat):
        return np.sum(submat)
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submat = matrix[i:k + 1, j:l + 1]
                    if get_submatrix_sum(submat) == -86:
                        result.append(submat)
    return result