import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, start_col, current_sum, current_matrix):
        if current_sum == 8:
            result.append(current_matrix)
            return
        if current_sum > 8 or start_row >= rows or start_col >= cols:
            return
        for row in range(start_row, rows):
            for col in range(start_col, cols):
                new_matrix = current_matrix + [matrix[row, col]] if not current_matrix else current_matrix + [matrix[row, col]]
                find_submatrices(row, col + 1, current_sum + matrix[row, col], new_matrix)
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, 0, [])
    return result