import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, start_row, start_col, end_row, end_col):
        total = 0
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                total += matrix[i][j]
        return total
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    if submatrix_sum(matrix, start_row, start_col, end_row, end_col) == 38:
                        result.append(matrix[start_row:end_row, start_col:end_col])
    return result