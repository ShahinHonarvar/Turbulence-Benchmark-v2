import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = -863
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top + 1, rows + 1):
                for right in range(left + 1, cols + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if submatrix.sum() == target_sum:
                        result.append(submatrix)
    return result