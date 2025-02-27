import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(m, start_row, end_row, start_col, end_col):
        sum_val = 0
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                sum_val += m[i][j]
        return sum_val

    def find_submatrices(m, target_sum):
        rows, cols = m.shape
        result = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        if sum_submatrix(m, start_row, end_row, start_col, end_col) == target_sum:
                            result.append(m[start_row:end_row + 1, start_col:end_col + 1])
        return result
    return find_submatrices(matrix, 66)