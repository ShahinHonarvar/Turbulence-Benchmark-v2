import numpy as np

def submatrix_with_n_numbers(matrix, n=59):
    rows, cols = matrix.shape
    count = 0
    for left in range(cols):
        for right in range(left, cols):
            for top in range(rows):
                for bottom in range(top, rows):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.size == n:
                        count += 1
    return count