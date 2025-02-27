import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def check_submatrix(r1, c1, r2, c2):
        return np.sum(matrix[r1:r2 + 1, c1:c2 + 1]) == -93
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if check_submatrix(r1, c1, r2, c2):
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result