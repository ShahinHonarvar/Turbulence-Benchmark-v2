import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for left in range(cols):
        for right in range(left, cols):
            for top in range(rows):
                for bottom in range(top, rows):
                    submatrix_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
                    if submatrix_sum == 78:
                        result.append(matrix[top:bottom + 1, left:right + 1])
    return result