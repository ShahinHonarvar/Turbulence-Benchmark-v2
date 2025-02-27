import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_95(sub):
        return np.sum(sub) == 95
    rows, cols = matrix.shape
    result = []
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r + 1, rows + 1):
                for c2 in range(c + 1, cols + 1):
                    sub = matrix[r:r2, c:c2]
                    if is_sum_95(sub):
                        result.append(sub)
    return result