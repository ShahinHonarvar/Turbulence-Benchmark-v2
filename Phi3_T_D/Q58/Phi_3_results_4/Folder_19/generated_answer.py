import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    count = 0
    for r_size in range(1, rows + 1):
        for c_size in range(1, cols + 1):
            for r in range(rows - r_size + 1):
                for c in range(cols - c_size + 1):
                    submatrix = matrix[r:r_size + r, c:c_size + c]
                    if submatrix.size == 17:
                        count += 1
    return count