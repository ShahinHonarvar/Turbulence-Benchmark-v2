import numpy as np

def submatrix_with_n_numbers(matrix):
    if not matrix.size or matrix.ndim != 2:
        return 0
    count = 0
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                flat_submatrix = submatrix.flatten()
                unique_values, counts = np.unique(flat_submatrix, return_counts=True)
                if np.any(counts == 39):
                    count += 1
    return count