import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for sub_row in range(rows):
        for sub_col in range(cols):
            for size in range(1, min(rows - sub_row, cols - sub_col) + 1):
                submat = mat[sub_row:sub_row + size, sub_col:sub_col + size]
                if np.all(submat == 38):
                    count += 1
    return count