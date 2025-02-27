import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    target_count = 191
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    if (x - i) * (y - j) == target_count:
                        submatrix = matrix[i:x, j:y]
                        if submatrix.size == target_count:
                            count += 1
    return count