import numpy as np

def submatrix_with_particular_sum(matrix):

    def check_submatrix_sum(submatrix, target_sum):
        return np.sum(submatrix) == target_sum
    rows, cols = matrix.shape
    target_sum = 394
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if check_submatrix_sum(submatrix, target_sum):
                        result.append(submatrix)
    return result