import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, row, col, rows, cols):
        submatrices = []
        for start_row in range(row, rows):
            for start_col in range(col, cols):
                current_sum = 0
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        current_sum += matrix[end_row][end_col]
                        if current_sum == target_sum:
                            submatrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
                        elif current_sum > target_sum:
                            break
        return submatrices
    target_sum = 87
    rows, cols = matrix.shape
    all_submatrices = []
    for row in range(rows):
        for col in range(cols):
            submatrices = find_submatrices(matrix, target_sum, row, col, rows, cols)
            all_submatrices.extend(submatrices)
    return all_submatrices