import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 35
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - target + 1):
        for j in range(cols - target + 1):
            submatrix = matrix[i:i + target, j:j + target]
            if submatrix.size == target:
                count += 1
    return count