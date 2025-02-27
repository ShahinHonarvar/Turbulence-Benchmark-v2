import numpy as np

def submatrix_with_particular_sum(matrix):
    if not matrix.size:
        return []
    result = []
    rows, cols = matrix.shape
    target_sum = -157
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if (bottom - top + 1) * (right - left + 1) <= target_sum:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        if submatrix.sum() == target_sum:
                            result.append(submatrix)
    return result