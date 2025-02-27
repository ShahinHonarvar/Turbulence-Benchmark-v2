import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            if matrix[r, c] == 77:
                for sub_row in range(r, rows):
                    for sub_col in range(c, cols):
                        if np.sum(matrix[r:sub_row + 1, c:sub_col + 1]) == 77:
                            count += 1
    return count