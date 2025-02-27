import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                submat_rows = rows - i
                submat_cols = cols - j
                for r in range(1, submat_rows + 1):
                    for c in range(1, submat_cols + 1):
                        if r * c == n:
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 87)