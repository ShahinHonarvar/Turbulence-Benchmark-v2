import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                for row_size in range(1, rows - i + 1):
                    for col_size in range(1, cols - j + 1):
                        if row_size * col_size == n:
                            if np.sum(mat[i:i + row_size, j:j + col_size]) == n * mat[i:i + row_size, j:j + col_size].mean():
                                count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 5)