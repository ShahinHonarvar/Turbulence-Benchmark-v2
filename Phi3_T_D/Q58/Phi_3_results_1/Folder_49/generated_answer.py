import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    rows, cols = matrix.shape
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            for i in range(rows - sub_rows + 1):
                for j in range(cols - sub_cols + 1):
                    submatrix = matrix[i:i + sub_rows, j:j + sub_cols]
                    if submatrix.size == 72:
                        count += 1
    return count