import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for row_end in range(i, rows):
                for col_end in range(j, cols):
                    if np.sum(matrix[i:row_end + 1, j:col_end + 1]) == 94:
                        result.append(matrix[i:row_end + 1, j:col_end + 1])
    return result