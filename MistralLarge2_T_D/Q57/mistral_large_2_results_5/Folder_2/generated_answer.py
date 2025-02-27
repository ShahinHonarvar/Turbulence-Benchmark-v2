import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    target_sum = -863
    submatrices = []

    def is_submatrix_sum_target(x1, y1, x2, y2):
        return np.sum(matrix[x1:x2 + 1, y1:y2 + 1]) == target_sum
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    if is_submatrix_sum_target(x1, y1, x2, y2):
                        submatrices.append(matrix[x1:x2 + 1, y1:y2 + 1])
    return submatrices