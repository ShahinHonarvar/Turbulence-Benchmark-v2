import numpy as np

def submatrix_with_particular_sum(matrix):
    total_rows, total_cols = matrix.shape
    results = []
    for i in range(total_rows):
        for j in range(total_cols):
            for k in range(i, total_rows):
                for l in range(j, total_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 616:
                        results.append(submatrix)
    return results