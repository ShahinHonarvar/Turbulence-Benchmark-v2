import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submat = matrix[top:bottom + 1, left:right + 1]
                    if np.sum(submat) == 66:
                        result.append(submat)
    return result