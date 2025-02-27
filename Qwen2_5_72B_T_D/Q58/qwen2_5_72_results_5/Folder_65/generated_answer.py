import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                submatrix_size = (rows - i) * (cols - j)
                if submatrix_size >= n and matrix[i:, j:].size >= n:
                    if matrix[i:i + 1, j:j + 34].size == n or matrix[i:i + 1, j:j + 35].size == n or matrix[i:i + 35, j:j + 1].size == n or (matrix[i:i + 34, j:j + 1].size == n):
                        count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 35)