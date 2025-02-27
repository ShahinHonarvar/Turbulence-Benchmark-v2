import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 3):
        for c in range(cols - 3):
            sub_matrix = matrix[r:r + 4, c:c + 4]
            if sub_matrix.size == 16:
                count += 1
    return count