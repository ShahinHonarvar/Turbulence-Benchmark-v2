import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.ndim != 2 or not issubclass(matrix.dtype.type, np.integer):
        return 0
    count = 0
    rows, cols = matrix.shape
    for r_start in range(rows):
        for c_start in range(cols):
            for r_end in range(r_start + 1, rows + 1):
                for c_end in range(c_start + 1, cols + 1):
                    submatrix = matrix[r_start:r_end, c_start:c_end]
                    if np.count_nonzero(submatrix == 1) == submatrix.size:
                        count += 1
    return count