import numpy as np

def count_sub_matrices(matrix):
    count = 0
    for sub_rows in range(1, matrix.shape[0] + 1):
        for sub_cols in range(1, matrix.shape[1] + 1):
            for top in range(matrix.shape[0] - sub_rows + 1):
                for left in range(matrix.shape[1] - sub_cols + 1):
                    sub_matrix = matrix[top:top + sub_rows, left:left + sub_cols]
                    if sub_matrix.size == 45:
                        count += 1
    return count

def submatrix_with_n_numbers(matrix):
    result = count_sub_matrices(matrix)
    return result