import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 85

    def count_elements_in_submatrix(submatrix):
        return submatrix.size
    rows, cols = matrix.shape
    count_of_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            for row_size in range(1, rows - i + 1):
                for col_size in range(1, cols - j + 1):
                    submatrix = matrix[i:i + row_size, j:j + col_size]
                    if count_elements_in_submatrix(submatrix) == target_count:
                        count_of_submatrices += 1
    return count_of_submatrices