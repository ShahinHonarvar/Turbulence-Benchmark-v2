import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, rows, cols, size):
        count = 0
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if (matrix[i:i + size, j:j + size] == 115).all():
                    count += 1
        return count
    rows, cols = matrix.shape
    n_elements = 115
    for size in range(1, min(rows, cols) + 1):
        if size * size == n_elements:
            return count_submatrices_of_size(matrix, rows, cols, size)
    return 0