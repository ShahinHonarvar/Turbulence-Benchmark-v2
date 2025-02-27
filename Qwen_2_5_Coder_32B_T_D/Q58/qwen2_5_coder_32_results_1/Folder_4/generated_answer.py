import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    n = 15
    if n > rows * cols:
        return 0
    for i in range(rows):
        for j in range(cols):
            for height in range(1, rows - i + 1):
                for width in range(1, cols - j + 1):
                    if height * width == n:
                        submatrix_count += 1
    return submatrix_count