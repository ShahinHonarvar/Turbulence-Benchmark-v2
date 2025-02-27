import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for width in range(1, cols - j + 1):
                    for height in range(1, rows - i + 1):
                        if width * height == n:
                            submatrix = mat[i:i + height, j:j + width]
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 146)