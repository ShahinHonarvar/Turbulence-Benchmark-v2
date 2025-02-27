import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = -64
    result_list = []
    rows, cols = matrix.shape

    def check_sum(submatrix):
        return np.sum(submatrix) == target_sum
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if check_sum(submatrix):
                        result_list.append(submatrix)
    return result_list