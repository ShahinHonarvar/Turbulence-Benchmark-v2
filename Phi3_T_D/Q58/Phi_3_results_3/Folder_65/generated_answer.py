import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    row_count, col_count = matrix.shape
    count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            for row_len in range(1, row_count - row_start + 1):
                if row_len < 35:
                    continue
                for col_len in range(1, col_count - col_start + 1):
                    if col_len < 35:
                        continue
                    if row_len * col_len == 35:
                        count += 1
    return count