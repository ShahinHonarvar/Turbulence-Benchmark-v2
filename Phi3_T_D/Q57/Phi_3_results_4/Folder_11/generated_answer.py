import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for left in range(cols):
        for right in range(left, cols):
            sum_cols = [0] * rows
            for top in range(rows):
                for bottom in range(top, rows):
                    sum_cols[bottom] += matrix[top][left:right + 1].sum()
                    if sum_cols[bottom] == 38:
                        result.append(matrix[top:bottom + 1, left:right + 1])
    return result