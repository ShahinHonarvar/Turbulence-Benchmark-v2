import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                sub = matrix[i:i + size, j:j + size]
                if sub.size == 90:
                    count += 1
    return count