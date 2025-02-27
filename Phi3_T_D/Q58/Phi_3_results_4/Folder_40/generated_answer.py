import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix.')
    if matrix.dtype != np.int:
        raise ValueError('Matrix elements must be integers.')
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r, c] == 1:
                count += 1
                size = 1
                while True:
                    end_pos = min(rows - r, cols - c)
                    for s in range(1, end_pos + 1):
                        if matrix[r + s - 1, c + s - 1] != 1:
                            break
                    else:
                        count += 1
                        continue
                    break
    return count