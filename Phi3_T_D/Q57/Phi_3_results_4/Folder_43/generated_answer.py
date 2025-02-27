import numpy as np

def submatrix_with_particular_sum(matrix):
    m = matrix.shape[0]
    n = matrix.shape[1]
    result = []

    def valid_sum(submat):
        return np.sum(submat) == -81

    def find_submatrices(r1, c1, r2, c2, current_sum=np.array([0])):
        if r1 <= r2 and c1 <= c2:
            submat = matrix[r1:r2 + 1, c1:c2 + 1]
            if valid_sum(submat):
                result.append(submat)
            sum_submat = current_sum + np.sum(submat)
            for new_r2 in range(r2, m):
                for new_c2 in range(c2, n):
                    find_submatrices(r1, c1, new_r2, new_c2, sum_submat)
    for row_start in range(m):
        for col_start in range(n):
            find_submatrices(row_start, col_start, row_start, col_start)
            find_submatrices(row_start, col_start, m - 1, col_start)
            find_submatrices(row_start, col_start, row_start, n - 1)
            find_submatrices(row_start, col_start, m - 1, n - 1)
    return result