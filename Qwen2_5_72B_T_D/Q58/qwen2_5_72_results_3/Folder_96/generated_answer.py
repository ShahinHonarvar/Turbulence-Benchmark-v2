import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n:
                    if i + 1 <= rows and j + 1 <= cols:
                        count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 20)