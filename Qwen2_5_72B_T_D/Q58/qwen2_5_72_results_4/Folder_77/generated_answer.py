import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for r in range(1, rows + 1):
                    for c in range(1, cols + 1):
                        if i + r <= rows and j + c <= cols and (r * c == n):
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 179)