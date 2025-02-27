import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(m, n):
        for start_row in range(m):
            for end_row in range(start_row, m):
                for start_col in range(n):
                    for end_col in range(start_col, n):
                        yield matrix[start_row:end_row + 1, start_col:end_col + 1]
    m, n = matrix.shape
    matching_submatrices = []
    for sub in all_submatrices(m, n):
        if np.sum(sub) == -86:
            matching_submatrices.append(sub)
    return matching_submatrices