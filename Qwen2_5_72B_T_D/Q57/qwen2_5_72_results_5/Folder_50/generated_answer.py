import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrix_sum(i, j, rows, cols, target, current_sum, submatrix, result, original_matrix):
        if current_sum == target:
            result.append(submatrix)
            return
        if current_sum > target or i >= rows or j >= cols:
            return
        new_element = original_matrix[i:i + 1, j:j + 1]
        find_submatrix_sum(i + 1, j, rows, cols, target, current_sum + new_element, submatrix + new_element, result, original_matrix)
        find_submatrix_sum(i, j + 1, rows, cols, target, current_sum + new_element, submatrix + new_element, result, original_matrix)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            find_submatrix_sum(i, j, rows, cols, 95, 0, np.array([]), result, matrix)
    return result