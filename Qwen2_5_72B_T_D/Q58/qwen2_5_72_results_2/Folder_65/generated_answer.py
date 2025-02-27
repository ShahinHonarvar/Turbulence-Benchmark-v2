import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for start_row in range(rows):
            for start_col in range(cols):
                if start_row + n <= rows and start_col + n <= cols:
                    submatrix = matrix[start_row:start_row + n, start_col:start_col + n]
                    if submatrix.size == 35:
                        count += 1
        return count
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    n = int(np.sqrt(35))
    if n * n != 35:
        return 0
    return count_submatrices_of_size(matrix, n)