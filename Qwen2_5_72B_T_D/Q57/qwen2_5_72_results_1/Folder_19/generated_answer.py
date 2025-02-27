import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target):
        result = []
        rows, cols = mat.shape
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                sum_temp = np.zeros(cols)
                for r in range(start_row, end_row + 1):
                    sum_temp += mat[r, :]
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        if np.sum(sum_temp[start_col:end_col + 1]) == target:
                            result.append(mat[start_row:end_row + 1, start_col:end_col + 1])
        return result
    return submatrix_sum(matrix, -97)