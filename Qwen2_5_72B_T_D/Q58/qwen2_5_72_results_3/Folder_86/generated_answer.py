import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for start_row in range(rows):
            for start_col in range(cols):
                if (start_row + 1) * (start_col + 1) == n:
                    if start_row + 1 <= rows and start_col + 1 <= cols:
                        count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 138)