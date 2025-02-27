import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    found_submatrices = []
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    submatrix_sum = np.sum(matrix[i:p + 1, j:q + 1])
                    if submatrix_sum == -26:
                        found_submatrices.append(matrix[i:p + 1, j:q + 1])
    return found_submatrices