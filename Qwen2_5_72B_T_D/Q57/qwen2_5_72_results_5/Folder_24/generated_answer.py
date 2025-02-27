import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target):
        rows, cols = (len(mat), len(mat[0]))
        result = []
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        sub_mat = mat[start_row:end_row, start_col:end_col]
                        if np.sum(sub_mat) == target:
                            result.append(sub_mat.tolist())
        return result
    return submatrix_sum(matrix, -36)