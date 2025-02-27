import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_valid(submatrix):
        return np.sum(submatrix) == 56

    def find_submatrices(matrix, valid_submatrices, current_row, current_col, rows, cols):
        if current_row > rows or current_col > cols:
            return
        for i in range(current_row, rows):
            for j in range(current_col, cols):
                for p in range(i, rows + 1):
                    for q in range(j, cols + 1):
                        sub = matrix[i:p, j:q]
                        if is_sum_valid(sub):
                            valid_submatrices.append(sub)
                find_submatrices(matrix, valid_submatrices, i + 1, j + 1, rows, cols)
    rows, cols = matrix.shape
    valid_submatrices = []
    find_submatrices(matrix, valid_submatrices, 0, 0, rows, cols)
    return valid_submatrices