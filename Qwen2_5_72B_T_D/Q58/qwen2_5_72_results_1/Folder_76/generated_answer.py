import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.size < 159:
        return 0
    rows, cols = matrix.shape
    possible_submatrices = 0
    for r_start in range(rows - 12 + 1):
        for c_start in range(cols - 12 + 1):
            if r_start + 12 <= rows and c_start + 12 <= cols:
                submatrix = matrix[r_start:r_start + 12, c_start:c_start + 12]
                if submatrix.size == 159:
                    possible_submatrices += 1
    return possible_submatrices