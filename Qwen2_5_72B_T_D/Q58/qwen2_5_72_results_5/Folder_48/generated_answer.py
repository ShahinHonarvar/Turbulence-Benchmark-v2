import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_size = 130
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (rows - i) * (cols - j) >= submatrix_size:
                for row_end in range(i + 1, rows + 1):
                    for col_end in range(j + 1, cols + 1):
                        if (row_end - i) * (col_end - j) == submatrix_size:
                            count += 1
    return count