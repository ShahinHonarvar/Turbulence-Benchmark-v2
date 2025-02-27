import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 97
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for size_i in range(1, height - i + 1):
                if size_i < n:
                    continue
                for size_j in range(1, width - j + 1):
                    if size_j < n:
                        continue
                    submatrix = matrix[i:i + size_i, j:j + size_j]
                    if submatrix.size == n:
                        count += 1
    return count