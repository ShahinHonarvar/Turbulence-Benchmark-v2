import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum, submatrices, start_row, start_col, end_row, end_col):
        current_sum = np.sum(mat[start_row:end_row, start_col:end_col])
        if current_sum == target_sum:
            submatrices.append(mat[start_row:end_row, start_col:end_col].tolist())
        if end_row < mat.shape[0]:
            submatrix_sum(mat, target_sum, submatrices, start_row, start_col, end_row + 1, end_col)
        if end_col < mat.shape[1]:
            submatrix_sum(mat, target_sum, submatrices, start_row, start_col, end_row, end_col + 1)
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix_sum(matrix, 41, submatrices, i, j, i + 1, j + 1)
    return submatrices