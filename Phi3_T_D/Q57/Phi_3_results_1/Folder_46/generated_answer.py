import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape

    def check_submatrix(r1, c1, r2, c2):
        return np.sum(matrix[r1:r2 + 1, c1:c2 + 1]) == 416
    for rows in range(n):
        for cols in range(m):
            for final_rows in range(rows, n + 1):
                for final_cols in range(cols, m + 1):
                    if check_submatrix(rows, cols, final_rows, final_cols):
                        submatrix = matrix[rows:final_rows + 1, cols:final_cols + 1]
                        submatrices.append(submatrix)
    return submatrices