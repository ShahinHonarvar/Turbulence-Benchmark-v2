import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(matrix):
        rows, cols = matrix.shape
        for r_idx in range(rows):
            for c_idx in range(cols):
                for size in range(1, rows - r_idx + 1):
                    for end_row in range(r_idx + size, rows + 1):
                        for end_col in range(c_idx + size, cols + 1):
                            yield matrix[r_idx:end_row, c_idx:end_col]
    return [submat for submat in get_all_submatrices(matrix) if np.sum(submat) == -87]