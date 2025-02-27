import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for row_size in range(1, rows - i + 1):
                    for col_size in range(1, cols - j + 1):
                        if row_size * col_size == n:
                            submatrix = mat[i:i + row_size, j:j + col_size]
                            if submatrix.size == n:
                                count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 19)