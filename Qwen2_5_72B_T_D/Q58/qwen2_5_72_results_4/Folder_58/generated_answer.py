import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n):
        rows, cols = m.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for size in range(1, min(rows - i, cols - j) + 1):
                    if size * size == n:
                        submatrix = m[i:i + size, j:j + size]
                        count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 185)