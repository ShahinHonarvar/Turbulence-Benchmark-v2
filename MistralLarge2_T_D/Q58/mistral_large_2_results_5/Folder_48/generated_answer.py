import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 130
    rows, cols = matrix.shape
    count = 0
    for top in range(rows):
        for bottom in range(top + 1, rows + 1):
            for left in range(cols):
                for right in range(left + 1, cols + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if submatrix.size == n:
                        count += 1
    return count