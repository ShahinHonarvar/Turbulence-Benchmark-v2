import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(start_row, start_col, current_sum, current_submatrix):
        if current_sum == -87:
            submatrices.append(current_submatrix)
            return
        if current_sum < -87 or start_row >= rows or start_col >= cols:
            return
        for i in range(start_row, rows):
            for j in range(start_col, cols):
                new_submatrix = current_submatrix + [(i, j)]
                find_submatrices(i, j + 1, current_sum + matrix[i, j], new_submatrix)
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, 0, [])
    result = []
    for submatrix in submatrices:
        submatrix_rows = [coord[0] for coord in submatrix]
        submatrix_cols = [coord[1] for coord in submatrix]
        min_row, max_row = (min(submatrix_rows), max(submatrix_rows))
        min_col, max_col = (min(submatrix_cols), max(submatrix_cols))
        result.append(matrix[min_row:max_row + 1, min_col:max_col + 1].tolist())
    return result