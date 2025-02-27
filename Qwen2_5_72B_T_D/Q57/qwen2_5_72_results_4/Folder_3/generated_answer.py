import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum):
        row, col = (len(mat), len(mat[0]))
        result = []
        for start_row in range(row):
            for end_row in range(start_row, row):
                for start_col in range(col):
                    for end_col in range(start_col, col):
                        current_sum = np.sum(mat[start_row:end_row + 1, start_col:end_col + 1])
                        if current_sum == target_sum:
                            result.append(mat[start_row:end_row + 1, start_col:end_col + 1].tolist())
        return result
    return submatrix_sum(matrix, 54)