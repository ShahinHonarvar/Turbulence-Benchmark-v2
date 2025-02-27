import numpy as np

def submatrix_with_particular_sum(matrix):

    def check_sum(top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if check_sum(top, left, bottom, right) == 394:
                        result.append(matrix[top:bottom + 1, left:right + 1])
    return result