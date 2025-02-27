import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_size = 56
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(1, rows - i + 1):
                for c in range(1, cols - j + 1):
                    submatrix = matrix[i:i + r, j:j + c]
                    if submatrix.size == target_size:
                        count += 1
    return count