import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for rows in range(n):
        for cols in range(m):
            for size_rows in range(1, n - rows + 1):
                for size_cols in range(1, m - cols + 1):
                    sub_matrix = matrix[rows:rows + size_rows, cols:cols + size_cols]
                    if np.sum(sub_matrix) == -185:
                        result.append(sub_matrix)
    return result