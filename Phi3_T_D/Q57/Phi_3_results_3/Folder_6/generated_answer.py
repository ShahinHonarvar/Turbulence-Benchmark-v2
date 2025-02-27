import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 126
    result = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top + 1, rows + 1):
                for right in range(left + 1, cols + 1):
                    submatrix_sum = np.sum(matrix[top:bottom, left:right])
                    if submatrix_sum == target_sum:
                        result.append(matrix[top:bottom, left:right])
    return result