import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(sub_matrix == 54) == 9:
                count += 1
    return count