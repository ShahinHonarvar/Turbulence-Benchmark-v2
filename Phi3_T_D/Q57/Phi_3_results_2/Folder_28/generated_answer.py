import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def check_sum(sub_matrix):
        return np.sum(sub_matrix) == 15

    def explore(i, j, current_submatrix):
        for rows_extend in range(i, rows + 1):
            for cols_extend in range(j, cols + 1):
                current_submatrix = matrix[i:rows_extend, j:cols_extend]
                if check_sum(current_submatrix):
                    submatrices.append(current_submatrix.tolist())
    for i in range(rows):
        for j in range(cols):
            explore(i, j, np.array([]))
    return submatrices