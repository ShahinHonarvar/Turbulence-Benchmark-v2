import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n):
        rows, cols = m.shape
        count = 0
        if rows * cols < n:
            return 0
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n or (rows - i) * (j + 1) == n or (i + 1) * (cols - j) == n or ((rows - i) * (cols - j) == n):
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 68)