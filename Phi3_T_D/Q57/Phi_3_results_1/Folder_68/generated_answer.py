import numpy as np

def submatrix_with_particular_sum(matrix):
    res = []
    rows, cols = matrix.shape
    for top in range(0, rows):
        for left in range(0, cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    sub = matrix[top:bottom + 1, left:right + 1]
                    if sub.sum() == 3:
                        res.append(sub)
    return res