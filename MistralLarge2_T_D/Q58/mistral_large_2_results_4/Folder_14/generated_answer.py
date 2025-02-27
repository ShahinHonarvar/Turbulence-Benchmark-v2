import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr in range(rows - r + 1):
                for dc in range(cols - c + 1):
                    submatrix = matrix[r:r + dr, c:c + dc]
                    if submatrix.size == 84:
                        count += 1
    return count