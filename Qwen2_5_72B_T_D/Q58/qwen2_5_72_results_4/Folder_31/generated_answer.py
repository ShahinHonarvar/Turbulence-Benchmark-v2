import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n):
        count = 0
        rows, cols = m.shape
        for i in range(rows):
            for j in range(cols):
                submatrix_size = 1
                while i + submatrix_size <= rows and j + submatrix_size <= cols:
                    submatrix = m[i:i + submatrix_size, j:j + submatrix_size]
                    if submatrix.size == n:
                        count += 1
                    submatrix_size += 1
        return count
    return count_submatrices_with_n_elements(matrix, 45)