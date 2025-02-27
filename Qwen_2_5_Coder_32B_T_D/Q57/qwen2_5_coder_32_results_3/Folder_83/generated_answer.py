import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for subrow in range(i + 1, rows + 1):
                for subcol in range(j + 1, cols + 1):
                    submatrix = matrix[i:subrow, j:subcol]
                    if np.sum(submatrix) == -15:
                        result.append(submatrix)
    return result