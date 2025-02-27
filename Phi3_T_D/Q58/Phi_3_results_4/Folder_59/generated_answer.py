import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 76
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i + 1, cols - j + 1) + 1):
                submatrix_sum = np.sum(matrix[i:i + size, j:j + size])
                if submatrix_sum == size * n:
                    count += 1
    return count