import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 432
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(start_row, start_col, current_sum, current_matrix):
        if current_sum == target_sum:
            submatrices.append(current_matrix)
            return
        row, col = (start_row, start_col)
        while row < rows and col < cols:
            end_row = min(rows, start_row + len(current_matrix))
            end_col = min(cols, start_col + len(current_matrix[0]))
            if row < end_row and col < end_col:
                current_sum += matrix[row][col]
                if current_sum <= target_sum:
                    current_matrix.append(matrix[row][col])
                    find_submatrices(start_row, start_col, current_sum, current_matrix.copy())
                    find_submatrices(start_row, col + 1, current_sum - matrix[row][col], current_matrix[:-1])
            row += 1
            col = start_col
    for start_row in range(rows):
        for start_col in range(cols):
            find_submatrices(start_row, start_col, 0, [])
    return submatrices