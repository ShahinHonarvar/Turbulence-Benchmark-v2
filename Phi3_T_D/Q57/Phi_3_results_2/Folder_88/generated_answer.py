import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def check_sum(sub_mat):
        return np.sum(sub_mat) == -64
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    sub_mat = matrix[i:k, j:l]
                    if check_sum(sub_mat):
                        result.append(sub_mat)
    return result