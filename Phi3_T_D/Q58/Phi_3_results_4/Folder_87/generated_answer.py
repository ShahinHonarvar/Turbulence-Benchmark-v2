import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 96
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for size in range(1, min(matrix.shape) + 1):
                if i + size <= matrix.shape[0] and j + size <= matrix.shape[1]:
                    submatrix = matrix[i:i + size, j:j + size]
                    if submatrix.size == n:
                        count += 1
    return count