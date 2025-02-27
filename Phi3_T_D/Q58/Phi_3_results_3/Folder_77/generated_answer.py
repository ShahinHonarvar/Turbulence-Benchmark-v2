import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')

    def count_submatrices(start, end, min_dim):
        count = 0
        for y in range(start + min_dim - 1, end - min_dim + 2):
            for x in range(start + min_dim - 1, end - min_dim + 2):
                submatrix = matrix[y - min_dim + 1:y + 1, x - min_dim + 1:x + 1]
                if submatrix.size == 179:
                    count += 1
        return count
    rows, cols = matrix.shape
    total_count = 0
    for min_dim in range(1, min(rows, cols) + 1):
        for i in range(rows - min_dim + 1):
            for j in range(cols - min_dim + 1):
                total_count += count_submatrices(i, j, min_dim)
    return total_count