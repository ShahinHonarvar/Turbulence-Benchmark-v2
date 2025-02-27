import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(mat):
        m, n = mat.shape
        submatrices = []
        for start_row in range(m):
            for start_col in range(n):
                for end_row in range(start_row + 1, m + 1):
                    for end_col in range(start_col + 1, n + 1):
                        submatrices.append(mat[start_row:end_row, start_col:end_col])
        return submatrices
    all_submatrices = get_all_submatrices(matrix)
    result = [submatrix for submatrix in all_submatrices if np.sum(submatrix) == 34]
    return result