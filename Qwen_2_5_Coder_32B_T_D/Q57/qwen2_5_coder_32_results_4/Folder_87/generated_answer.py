import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_of_submatrix(sub):
        return np.sum(sub)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if sum_of_submatrix(submatrix) == 35:
                        result.append(submatrix)
    return result