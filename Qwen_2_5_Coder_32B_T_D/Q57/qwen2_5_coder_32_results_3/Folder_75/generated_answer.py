import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(i, j, p, q):
        return np.sum(matrix[i:p + 1, j:q + 1])
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    if get_submatrix_sum(i, j, p, q) == 16:
                        result.append(matrix[i:p + 1, j:q + 1])
    return result