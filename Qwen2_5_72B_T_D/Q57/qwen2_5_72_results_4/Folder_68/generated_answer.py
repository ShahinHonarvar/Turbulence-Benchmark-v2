import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, top_left, bottom_right):
        submatrix = matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]
        return (submatrix, np.sum(submatrix))
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submat, subsum = submatrix_sum(matrix, (i, j), (k, l))
                    if subsum == 3:
                        result.append(submat)
    return result