import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_correct(submatrix, target_sum):
        return np.sum(submatrix) == target_sum

    def find_submatrices(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        if is_sum_correct(submatrix, target_sum):
                            submatrices.append(submatrix)
        return submatrices
    target_sum = 78
    return find_submatrices(matrix, target_sum)