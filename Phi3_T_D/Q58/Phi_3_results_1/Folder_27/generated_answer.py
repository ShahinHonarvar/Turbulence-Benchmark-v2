import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for height in range(1, rows - r + 1):
                for width in range(1, cols - c + 1):
                    submatrix = matrix[r:r + height, c:c + width]
                    if submatrix.size == 77:
                        count += 1
    return count