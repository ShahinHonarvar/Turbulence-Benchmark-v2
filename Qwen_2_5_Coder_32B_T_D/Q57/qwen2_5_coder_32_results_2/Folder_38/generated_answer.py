import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for end_row in range(i + 1, rows + 1):
                for end_col in range(j + 1, cols + 1):
                    submatrix = matrix[i:end_row, j:end_col]
                    if np.sum(submatrix) == 34:
                        result.append(submatrix)
    return result