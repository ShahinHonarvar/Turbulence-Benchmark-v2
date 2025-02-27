import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(matrix, target):
        row, col = matrix.shape
        submatrices = []
        for start_row in range(row):
            for end_row in range(start_row, row):
                for start_col in range(col):
                    for end_col in range(start_col, col):
                        if matrix[start_row:end_row + 1, start_col:end_col + 1].sum() == target:
                            submatrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
        return submatrices
    return find_submatrices_with_sum(matrix, 64)