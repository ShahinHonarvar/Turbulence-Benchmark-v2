import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 56
    result = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.sum() == target_sum:
                        result.append(submatrix)
    return result