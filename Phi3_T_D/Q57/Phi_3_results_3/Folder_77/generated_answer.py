import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i + 1, cols - j + 1) + 1):
                sub_matrix = matrix[i:i + size, j:j + size]
                if sub_matrix.sum() == -336:
                    sub_matrices.append(sub_matrix)
    return sub_matrices