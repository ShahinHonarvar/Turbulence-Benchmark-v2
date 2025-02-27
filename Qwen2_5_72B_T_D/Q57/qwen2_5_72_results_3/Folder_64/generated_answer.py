import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(start_row, start_col, end_row, end_col):
        submatrices = []
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                submatrix = matrix[i:end_row + 1, j:end_col + 1]
                submatrices.append(submatrix)
        return submatrices
    rows, cols = matrix.shape
    target_sum = -4
    valid_submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrices = generate_submatrices(i, j, k, l)
                    for sub in submatrices:
                        if np.sum(sub) == target_sum:
                            valid_submatrices.append(sub)
    return valid_submatrices