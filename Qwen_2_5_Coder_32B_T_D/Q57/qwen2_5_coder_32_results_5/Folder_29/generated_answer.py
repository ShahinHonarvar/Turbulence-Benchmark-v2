import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix(i, j, p, q):
        return matrix[i:p + 1, j:q + 1]
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    submatrix = get_submatrix(i, j, p, q)
                    if np.sum(submatrix) == 84:
                        result.append(submatrix)
    return result