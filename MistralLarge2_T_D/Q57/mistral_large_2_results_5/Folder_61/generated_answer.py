import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, start_col, sub_sum, current_matrix):
        if sub_sum == 8:
            result.append(current_matrix)
            return
        if sub_sum > 8 or start_row >= rows or start_col >= cols:
            return
        for i in range(start_row, rows):
            for j in range(start_col, cols):
                new_matrix = np.copy(current_matrix)
                new_matrix[i, j] = matrix[i, j]
                find_submatrices(i, j + 1, sub_sum + matrix[i, j], new_matrix)
    for i in range(rows):
        for j in range(cols):
            empty_matrix = np.zeros_like(matrix)
            find_submatrices(i, j, 0, empty_matrix)
    return result