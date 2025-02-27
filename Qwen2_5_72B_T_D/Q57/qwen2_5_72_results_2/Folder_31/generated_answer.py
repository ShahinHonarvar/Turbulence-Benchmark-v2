import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrices(mat, target_sum):
        rows, cols = (len(mat), len(mat[0]))
        result = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submatrix_sum = np.sum(mat[start_row:end_row + 1, start_col:end_col + 1])
                        if submatrix_sum == target_sum:
                            result.append(mat[start_row:end_row + 1, start_col:end_col + 1])
        return result
    return sum_submatrices(matrix, -44)