import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr in range(r, rows):
                for dc in range(c, cols):
                    submatrix = matrix[r:dr + 1, c:dc + 1]
                    if submatrix.size == 15:
                        count += 1
    return count