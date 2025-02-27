import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, submatrices, start_row, start_col, rows, cols):
        for end_row in range(start_row, rows):
            for end_col in range(start_col, cols):
                current_sum = np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
                if current_sum == target_sum:
                    submatrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
    target_sum = 8
    submatrices = []
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            find_submatrices(matrix, target_sum, submatrices, start_row, start_col, rows, cols)
    return submatrices