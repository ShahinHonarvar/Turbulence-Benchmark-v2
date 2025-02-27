import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(m):
        rows, cols = m.shape
        submatrices = []
        for row_start in range(rows):
            for col_start in range(cols):
                for row_len in range(1, rows - row_start + 1):
                    for col_len in range(1, cols - col_start + 1):
                        submatrix = m[row_start:row_start + row_len, col_start:col_start + col_len]
                        submatrices.append(submatrix)
        return submatrices
    target_sum = 862
    submatrices = all_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == target_sum]
    return result