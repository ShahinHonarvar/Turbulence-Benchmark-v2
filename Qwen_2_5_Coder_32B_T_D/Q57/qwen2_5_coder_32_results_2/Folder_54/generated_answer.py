import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(submatrix):
        return np.sum(submatrix)
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if get_submatrix_sum(submatrix) == -59:
                        result.append(submatrix.tolist())
    return result