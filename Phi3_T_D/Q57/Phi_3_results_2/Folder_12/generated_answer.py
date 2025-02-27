import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for row_len in range(1, rows - row_start + 1):
                for col_len in range(1, cols - col_start + 1):
                    submatrix = matrix[row_start:row_start + row_len, col_start:col_start + col_len]
                    if submatrix.sum() == -83:
                        results.append(submatrix.tolist())
    return results