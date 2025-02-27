import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row_offset in range(rows):
        for col_offset in range(cols):
            for subrows in range(1, rows - row_offset + 1):
                for subcols in range(1, cols - col_offset + 1):
                    submatrix = matrix[row_offset:row_offset + subrows, col_offset:col_offset + subcols]
                    if submatrix.size == 115:
                        count += 1
    return count