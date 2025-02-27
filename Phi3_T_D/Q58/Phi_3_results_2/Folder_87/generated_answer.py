import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    count = 0
    rows, cols = matrix.shape
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            for r in range(rows - sub_rows + 1):
                for c in range(cols - sub_cols + 1):
                    submatrix = matrix[r:r + sub_rows, c:c + sub_cols]
                    if submatrix.size == 96:
                        count += 1
    return count