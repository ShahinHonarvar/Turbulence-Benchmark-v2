import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for subrows in range(i + 1, rows + 1):
                for subcols in range(j + 1, cols + 1):
                    submatrix = matrix[i:subrows, j:subcols]
                    if np.sum(submatrix) == 8:
                        result.append(submatrix)
    return result