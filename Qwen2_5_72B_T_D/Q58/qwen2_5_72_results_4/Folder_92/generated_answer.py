import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                if i + 1 <= rows and j + n // (i + 1) <= cols and ((i + 1) * (n // (i + 1)) == n):
                    submatrix = mat[i:i + 1, j:j + n // (i + 1)]
                    if submatrix.size == 8:
                        count += 1
        return count
    result = count_submatrices_with_n_elements(matrix, 8)
    return result