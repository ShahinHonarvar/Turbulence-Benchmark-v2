import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_size = 49
    rows, cols = matrix.shape
    for i in range(rows - 6 + 1):
        for j in range(cols - 6 + 1):
            submatrix = matrix[i:i + 7, j:j + 7]
            if submatrix.size == target_size:
                count += 1
    return count