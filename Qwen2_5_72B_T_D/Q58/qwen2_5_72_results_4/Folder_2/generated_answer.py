import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        if (end_row - start_row) * (end_col - start_col) == n:
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 107)