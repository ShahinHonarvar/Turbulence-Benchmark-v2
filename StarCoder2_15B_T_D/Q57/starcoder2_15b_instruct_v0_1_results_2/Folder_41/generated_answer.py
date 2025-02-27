import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for start_row in range(matrix.shape[0]):
        for start_col in range(matrix.shape[1]):
            for submatrix_size in range(1, min(matrix.shape[0] - start_row, matrix.shape[1] - start_col) + 1):
                submatrix = matrix[start_row:start_row + submatrix_size, start_col:start_col + submatrix_size]
                if np.sum(submatrix) == -26:
                    result.append(submatrix)
    return result