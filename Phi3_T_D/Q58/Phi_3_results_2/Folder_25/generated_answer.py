import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 6
    rows_sub = cols_sub = n
    while rows_sub <= rows and cols_sub <= cols:
        for i in range(rows - rows_sub + 1):
            for j in range(cols - cols_sub + 1):
                if np.all(matrix[i:i + rows_sub, j:j + cols_sub] == n):
                    count += 1
        rows_sub += 1
        if rows_sub > rows:
            rows_sub = rows
        cols_sub += 1
        if cols_sub > cols:
            cols_sub = cols
    return count