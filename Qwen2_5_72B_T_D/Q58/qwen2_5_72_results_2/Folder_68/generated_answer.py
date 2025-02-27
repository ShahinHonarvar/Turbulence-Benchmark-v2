import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                submatrix_size = (min(rows - i, cols - j), min(rows - i, cols - j))
                elements_counted = 0
                while elements_counted < n and submatrix_size[0] > 0 and (submatrix_size[1] > 0):
                    submatrix = mat[i:i + submatrix_size[0], j:j + submatrix_size[1]]
                    if submatrix.size == n:
                        count += 1
                    elements_counted = submatrix.size
                    submatrix_size = (submatrix_size[0] - 1, submatrix_size[1] - 1)
        return count
    return count_submatrices_with_n_elements(matrix, 74)