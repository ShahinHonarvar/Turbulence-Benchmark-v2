import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_size(matrix, target_size):
        count = 0
        rows, cols = matrix.shape
        for row_start in range(rows - target_size + 1):
            for col_start in range(cols - target_size + 1):
                submatrix = matrix[row_start:row_start + target_size, col_start:col_start + target_size]
                if submatrix.size == target_size:
                    count += 1
        return count
    return count_submatrices_with_size(matrix, 107)