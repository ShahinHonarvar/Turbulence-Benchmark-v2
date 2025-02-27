import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_two(matrix, start_row, start_col, rows, cols):
        count = 0
        for i in range(start_row, rows - 1):
            for j in range(start_col, cols - 1):
                submatrix = matrix[i:i + 2, j:j + 2]
                unique_numbers = np.unique(submatrix)
                if len(unique_numbers) == 2:
                    count += 1
        return count
    rows, cols = matrix.shape
    return count_submatrices_with_two(matrix, 0, 0, rows, cols)