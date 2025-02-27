import numpy as np

def submatrix_with_n_numbers(matrix):
    if isinstance(matrix, np.ndarray) and len(matrix.shape) == 2:
        rows, cols = matrix.shape
        count = 0
        for subrow in range(rows):
            for subcol in range(cols):
                for size in range(1, rows - subrow + 1):
                    for subsize in range(1, cols - subcol + 1):
                        submatrix = matrix[subrow:subrow + size, subcol:subcol + subsize]
                        if submatrix.size == 127:
                            count += 1
        return count
    else:
        return 0