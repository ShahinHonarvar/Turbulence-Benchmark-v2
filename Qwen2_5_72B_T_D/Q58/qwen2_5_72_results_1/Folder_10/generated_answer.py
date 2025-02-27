import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        rows, cols = matrix.shape
        for start_row in range(rows - size + 1):
            for start_col in range(cols - size + 1):
                submatrix = matrix[start_row:start_row + size, start_col:start_col + size]
                if submatrix.size == 56:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, int(np.sqrt(56)))