import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row, col, rows, cols, matrix, current, result):
        for start_row in range(row, rows):
            for start_col in range(col, cols):
                sum_val = 0
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        sum_val += matrix[end_row][end_col]
                        if sum_val == -61:
                            result.append(current[start_row - start_row:][start_col - start_col:])
    rows, cols = matrix.shape
    result = []
    find_submatrices(0, 0, rows, cols, matrix, matrix, result)
    return result