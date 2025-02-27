import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum):
        rows, cols = (len(mat), len(mat[0]))
        submatrices = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        current_sum = np.sum(mat[start_row:end_row + 1, start_col:end_col + 1])
                        if current_sum == target_sum:
                            submatrices.append(mat[start_row:end_row + 1, start_col:end_col + 1])
        return submatrices
    return submatrix_sum(matrix, 13)