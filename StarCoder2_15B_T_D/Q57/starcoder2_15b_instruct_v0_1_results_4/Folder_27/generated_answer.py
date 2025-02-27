import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    sub_matrix = matrix[r:i + 1, c:j + 1]
                    if np.sum(sub_matrix) == 77:
                        result.append(sub_matrix)
    return result