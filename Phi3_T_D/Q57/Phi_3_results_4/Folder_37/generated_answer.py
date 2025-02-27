import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.sum() == -82:
                        results.append(submatrix)
    return results