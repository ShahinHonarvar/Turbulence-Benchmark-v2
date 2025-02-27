import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 180
    if n > matrix.size:
        return 0
    row, col = matrix.shape
    count = 0
    submatrix_size = int(n / (row if row < col else col))
    if submatrix_size * row != n and submatrix_size * col != n:
        return 0
    for start_row in range(row - submatrix_size + 1):
        for start_col in range(col - submatrix_size + 1):
            submatrix = matrix[start_row:start_row + submatrix_size, start_col:start_col + submatrix_size]
            if submatrix.size == n:
                count += 1
    return count