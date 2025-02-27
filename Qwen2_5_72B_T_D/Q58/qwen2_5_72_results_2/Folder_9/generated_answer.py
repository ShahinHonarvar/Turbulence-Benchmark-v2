import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for h in range(1, rows - i + 1):
                    for w in range(1, cols - j + 1):
                        if h * w == n:
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 33)