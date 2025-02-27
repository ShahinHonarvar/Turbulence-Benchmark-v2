import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum):
        row, col = (len(mat), len(mat[0]))
        result = []
        for start_row in range(row):
            for start_col in range(col):
                for end_row in range(start_row + 1, row + 1):
                    for end_col in range(start_col + 1, col + 1):
                        if np.sum(mat[start_row:end_row, start_col:end_col]) == target_sum:
                            result.append(mat[start_row:end_row, start_col:end_col].tolist())
        return result
    return submatrix_sum(matrix, -63)