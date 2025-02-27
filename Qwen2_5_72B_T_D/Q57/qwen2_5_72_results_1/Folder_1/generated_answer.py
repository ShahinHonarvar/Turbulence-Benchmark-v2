import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_of_submatrix(mat, top_left, bottom_right):
        rows, cols = mat.shape
        i1, j1 = top_left
        i2, j2 = bottom_right
        if i2 >= rows or j2 >= cols:
            return None
        submat = mat[i1:i2 + 1, j1:j2 + 1]
        return (submat, np.sum(submat))
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submat, subsum = sum_of_submatrix(matrix, (i, j), (k, l))
                    if subsum == -25:
                        result.append(submat)
    return result