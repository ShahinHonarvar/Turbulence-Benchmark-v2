import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            row_sums = np.cumsum(matrix[i:], axis=0)
            for k in range(i, rows):
                col_sums = np.cumsum(matrix[:, j:k + 1], axis=1)
                for l in range(j, cols):
                    submatrix_sum = row_sums[k, l] - (row_sums[k, j] if k - i > 0 else 0) - (col_sums[k, l] - (col_sums[i, l] if l - j > 0 else 0))
                    if submatrix_sum == -44:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices