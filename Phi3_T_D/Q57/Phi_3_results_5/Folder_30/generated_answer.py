import numpy as np

def submatrix_with_particular_sum(matrix):

    def check_submatrix(row_ranges, col_ranges):
        return sum(matrix[r1:r2 + 1, c1:c2 + 1].flatten()) == 21
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if check_submatrix((i, k), (j, l)):
                        submatrices.append(matrix[i:k + 1, j:l + 1].tolist())
    return submatrices