import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for row_end in range(i + 1, rows + 1):
                    for col_end in range(j + 1, cols + 1):
                        submatrix = matrix[i:row_end, j:col_end]
                        if submatrix.size == n:
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 35)