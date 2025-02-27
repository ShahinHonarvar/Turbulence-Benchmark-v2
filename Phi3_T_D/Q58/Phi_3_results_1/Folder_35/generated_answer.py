import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    for x in range(rows):
        for y in range(cols):
            for size_x in range(1, rows - x + 1):
                for size_y in range(1, cols - y + 1):
                    submatrix = matrix[x:x + size_x, y:y + size_y]
                    if submatrix.size == 111:
                        count += 1
    return count