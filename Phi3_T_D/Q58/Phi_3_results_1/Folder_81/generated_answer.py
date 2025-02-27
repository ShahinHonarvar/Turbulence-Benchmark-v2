import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 97
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                non_zero_count = np.count_nonzero(submatrix)
                if non_zero_count == size ** 2:
                    count += 1
    return count