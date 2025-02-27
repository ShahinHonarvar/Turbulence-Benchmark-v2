import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def is_submatrix_sum_78(submatrix):
        return np.sum(submatrix) == 78
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if is_submatrix_sum_78(submatrix):
                        result.append(submatrix)
    return result