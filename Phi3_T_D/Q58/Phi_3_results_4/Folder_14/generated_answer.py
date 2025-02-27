import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for size_r in range(1, height + 1):
        for size_c in range(1, width + 1):
            for i in range(height - size_r + 1):
                for j in range(width - size_c + 1):
                    submatrix = matrix[i:i + size_r, j:j + size_c]
                    if submatrix.size == 84:
                        count += 1
    return count