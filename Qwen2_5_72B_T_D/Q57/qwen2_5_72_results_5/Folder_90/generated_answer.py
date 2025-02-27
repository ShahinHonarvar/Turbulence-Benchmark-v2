import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        row, col = (len(mat), len(mat[0]))
        result = []
        for start_row in range(row):
            for start_col in range(col):
                for end_row in range(start_row, row):
                    for end_col in range(start_col, col):
                        submatrix = mat[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    return find_submatrices_with_sum(matrix, -452)