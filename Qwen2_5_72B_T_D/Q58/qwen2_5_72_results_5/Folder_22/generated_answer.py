import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                for row_end in range(i + 1, rows + 1):
                    for col_end in range(j + 1, cols + 1):
                        if (row_end - i) * (col_end - j) == n:
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 21)