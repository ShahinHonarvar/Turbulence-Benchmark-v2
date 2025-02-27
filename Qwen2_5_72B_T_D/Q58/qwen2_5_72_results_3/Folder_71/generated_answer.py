import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 78
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == target_count:
                    count += 1
    return count