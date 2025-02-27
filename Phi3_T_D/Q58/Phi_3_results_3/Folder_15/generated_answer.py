import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(1, rows - i + 1):
                for l in range(1, cols - j + 1):
                    submatrix = matrix[i:i + k, j:j + l]
                    flat_submatrix = submatrix.flatten()
                    unique_elements = len(np.unique(flat_submatrix))
                    if unique_elements == 2:
                        count += 1
    return count