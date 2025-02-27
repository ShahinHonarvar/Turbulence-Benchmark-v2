import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_equal(submatrix, target):
        return np.sum(submatrix) == target
    rows, cols = matrix.shape
    target_sum = 19
    result = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    submatrix = matrix[i:x, j:y]
                    if is_sum_equal(submatrix, target_sum):
                        result.append(submatrix)
    return result