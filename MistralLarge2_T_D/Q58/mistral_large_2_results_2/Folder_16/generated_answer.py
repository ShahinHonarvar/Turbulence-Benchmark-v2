import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0

    def count_submatrices(start_row, start_col, end_row, end_col):
        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
        return np.count_nonzero(submatrix)
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if count_submatrices(i, j, k, l) == 154:
                        count += 1
    return count