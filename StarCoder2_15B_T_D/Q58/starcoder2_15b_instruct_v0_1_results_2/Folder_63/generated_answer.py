import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_integers = 57
    count = 0
    for row_start in range(num_rows):
        for col_start in range(num_cols):
            for row_end in range(row_start, num_rows):
                for col_end in range(col_start, num_cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    num_integers_in_submatrix = np.size(submatrix)
                    if num_integers_in_submatrix == num_integers:
                        count += 1
    return count