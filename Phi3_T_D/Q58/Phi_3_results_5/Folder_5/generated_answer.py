import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 63
    for left in range(cols):
        for top in range(rows):
            for width in range(1, cols - left + 1):
                for height in range(1, rows - top + 1):
                    submatrix = matrix[top:top + height, left:left + width]
                    if submatrix.size == n:
                        count += 1
    return count