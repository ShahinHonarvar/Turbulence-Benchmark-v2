import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 95
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for size in range(1, min(matrix.shape[0] - i, matrix.shape[1] - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.unique(submatrix).size == target_count:
                    count += 1
    return count