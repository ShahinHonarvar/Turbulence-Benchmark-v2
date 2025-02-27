import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submat, target):
        return np.sum(submat) == target
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submat = matrix[i:k, j:l]
                    if submatrix_sum(submat, 34):
                        result.append(submat)
    return result