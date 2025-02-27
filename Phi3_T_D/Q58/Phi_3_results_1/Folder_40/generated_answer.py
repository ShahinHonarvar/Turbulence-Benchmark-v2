import numpy as np

def submatrix_with_n_numbers(matrix, n=1):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == n:
                for sz in range(1, min(rows - i, cols - j) + 1):
                    submatrix_sum = np.sum(matrix[i:i + sz, j:j + sz])
                    if submatrix_sum == n * sz ** 2:
                        count += 1
    return count