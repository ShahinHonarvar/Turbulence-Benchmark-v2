import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def calculate_sum(top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if calculate_sum(top, left, bottom, right) == -25:
                        result.append(matrix[top:bottom + 1, left:right + 1])
    return result