import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            for block_size in range(1, min(len(matrix) - row_idx, len(matrix[0]) - col_idx) + 1):
                submatrix = matrix[row_idx:row_idx + block_size, col_idx:col_idx + block_size]
                if (submatrix == 1).all():
                    count += 1
    return count