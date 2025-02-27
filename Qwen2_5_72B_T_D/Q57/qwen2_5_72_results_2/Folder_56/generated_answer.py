import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, start_row, start_col, rows, cols, result):
        for i in range(start_row, rows):
            for j in range(start_col, cols):
                if np.sum(mat[start_row:i + 1, start_col:j + 1]) == target_sum:
                    result.append(mat[start_row:i + 1, start_col:j + 1])
    result = []
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            find_submatrices_with_sum(matrix, -50, i, j, rows, cols, result)
    return result