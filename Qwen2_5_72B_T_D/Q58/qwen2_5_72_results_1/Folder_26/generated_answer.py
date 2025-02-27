import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n):
        count = 0
        rows, cols = m.shape
        for i in range(rows):
            for j in range(cols):
                if (rows - i) * (cols - j) >= n:
                    submatrix = m[i:i + (n - 1) // (cols - j) + 1, j:j + (n - 1) // (rows - i + 1)]
                    if submatrix.size == n:
                        count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 115)