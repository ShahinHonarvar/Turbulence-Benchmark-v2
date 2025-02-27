import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            for submatrix_size in range(1, min(len(matrix) - row_index, len(matrix[row_index]) - col_index) + 1):
                submatrix = matrix[row_index:row_index + submatrix_size, col_index:col_index + submatrix_size]
                if submatrix.sum() == 27:
                    submatrices.append(submatrix)
    return submatrices