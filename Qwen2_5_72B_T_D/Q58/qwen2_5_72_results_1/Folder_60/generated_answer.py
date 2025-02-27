import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 88
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target:
                count += 1
    submatrix_counts = 0
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.sum(matrix[i:i + size, j:j + size] == target) == 88:
                    submatrix_counts += 1
    return submatrix_counts