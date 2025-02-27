import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    submatrix_count = 0
    for sub_h in range(1, height + 1):
        for sub_w in range(1, width + 1):
            for i in range(height - sub_h + 1):
                for j in range(width - sub_w + 1):
                    submatrices = matrix[i:i + sub_h, j:j + sub_w]
                    if len(submatrices.ravel()) == 120:
                        submatrix_count += 1
    return submatrix_count