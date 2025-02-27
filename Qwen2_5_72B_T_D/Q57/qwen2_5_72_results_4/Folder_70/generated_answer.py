import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, current_row, current_col, current_sum, current_submatrix, submatrices):
        rows, cols = mat.shape
        if current_row >= rows or current_col >= cols:
            return
        current_sum += mat[current_row, current_col]
        current_submatrix.append(mat[current_row, current_col])
        if current_sum == target_sum:
            submatrices.append(current_submatrix.copy())
        elif current_sum < target_sum:
            find_submatrices_with_sum(mat, target_sum, current_row + 1, current_col, current_sum, current_submatrix, submatrices)
            find_submatrices_with_sum(mat, target_sum, current_row, current_col + 1, current_sum, current_submatrix, submatrices)
        current_submatrix.pop()
        find_submatrices_with_sum(mat, target_sum, current_row + 1, current_col, 0, [], submatrices)
        find_submatrices_with_sum(mat, target_sum, current_row, current_col + 1, 0, [], submatrices)
    target_sum = 411
    submatrices = []
    find_submatrices_with_sum(matrix, target_sum, 0, 0, 0, [], submatrices)
    return submatrices