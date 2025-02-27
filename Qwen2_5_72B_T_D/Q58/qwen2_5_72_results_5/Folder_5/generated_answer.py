import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        count = 0
        rows, cols = matrix.shape
        target_size = int(np.sqrt(n))
        for start_row in range(rows - target_size + 1):
            for start_col in range(cols - target_size + 1):
                submatrix = matrix[start_row:start_row + target_size, start_col:start_col + target_size]
                if submatrix.size == n:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 63)