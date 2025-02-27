import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    total_submatrices = rows * (rows + 1) // 2 * (cols * (cols + 1)) // 2
    for i in range(rows):
        for j in range(cols):
            min_size = min(rows - i, cols - j)
            for size in range(1, min_size + 1):
                if np.sum(matrix[i:i + size, j:j + size]) == 60:
                    count += 1
    return count