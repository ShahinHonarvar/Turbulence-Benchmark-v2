import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(start_row, start_col, target_sum):
        current_sum = matrix[start_row, start_col]
        if current_sum == target_sum:
            submatrices.append(matrix[start_row:start_row + 1, start_col:start_col + 1])
        for row in range(start_row, rows):
            for col in range(start_col, cols):
                if current_sum + matrix[row, col] <= target_sum:
                    current_sum += matrix[row, col]
                    if current_sum == target_sum:
                        submatrices.append(matrix[start_row:row + 1, start_col:col + 1])
        return submatrices
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, 92)
    return submatrices