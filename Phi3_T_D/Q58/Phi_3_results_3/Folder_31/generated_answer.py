import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        raise ValueError('Input must be a two-dimensional matrix')
    rows, cols = matrix.shape
    count = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for size in range(1, min(rows - start_row, cols - start_col) + 1):
                submatrix = matrix[start_row:start_row + size, start_col:start_col + size]
                unique_integers = len(np.unique(submatrix))
                if unique_integers == 45:
                    count += 1
    return count