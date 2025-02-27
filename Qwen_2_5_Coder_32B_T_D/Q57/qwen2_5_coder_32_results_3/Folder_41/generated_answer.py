import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m, n = matrix.shape
    for start_row in range(m):
        for start_col in range(n):
            for end_row in range(start_row, m):
                for end_col in range(start_col, n):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if submatrix.sum() == -26:
                        result.append(submatrix)
    return result