import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    num_rows, num_cols = matrix.shape
    max_size = min(num_rows, num_cols)
    for size in range(1, max_size + 1):
        for i in range(num_rows - size + 1):
            for j in range(num_cols - size + 1):
                submat = matrix[i:i + size, j:j + size]
                if submat.sum() == -44:
                    result.append(submat)
    return result