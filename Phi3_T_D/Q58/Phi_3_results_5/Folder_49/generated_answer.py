import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 72
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if bottom - top + 1 == n and right - left + 1 == n:
                        if np.all(matrix[top:bottom + 1, left:right + 1]):
                            count += 1
    return count