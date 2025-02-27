import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    num_rows, num_cols = matrix.shape
    num_elements_in_submatrix = 130
    num_submatrices = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            num_elements = np.count_nonzero(~np.isnan(submatrix))
            if num_elements == num_elements_in_submatrix:
                num_submatrices += 1
    return num_submatrices