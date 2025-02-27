import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submat, target):
        return np.sum(submat) == target
    rows, cols = matrix.shape
    target_sum = -90
    result = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    submat = matrix[i:x, j:y]
                    if submatrix_sum(submat, target_sum):
                        result.append(submat)
    return result