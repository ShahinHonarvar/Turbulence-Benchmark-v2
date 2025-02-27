import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0

    def count_valid_submatrices(squares):
        return sum((1 for row in squares for submat in np.split(row, [18, 36]) if len(submat) == 18))
    num_rows, num_cols = matrix.shape
    max_submatrix_size = min(num_rows, num_cols)
    count = 0
    for size in range(1, max_submatrix_size + 1):
        for row in range(num_rows - size + 1):
            for col in range(num_cols - size + 1):
                submat = matrix[row:row + size, col:col + size]
                if count_valid_submatrices(submat):
                    count += 1
    return count