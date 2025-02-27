import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix(i, j, p, q):
        return matrix[i:p + 1, j:q + 1]
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    if np.sum(get_submatrix(i, j, p, q)) == -128:
                        result.append(get_submatrix(i, j, p, q))
    return result