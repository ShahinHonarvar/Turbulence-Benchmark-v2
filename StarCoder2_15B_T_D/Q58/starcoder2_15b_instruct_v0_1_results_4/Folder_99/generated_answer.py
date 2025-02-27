import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    num_elements = 146
    matrix_rows, matrix_cols = matrix.shape
    for i in range(matrix_rows - 2):
        for j in range(matrix_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            num_elements_in_submatrix = np.count_nonzero(~np.isnan(submatrix))
            if num_elements_in_submatrix == num_elements:
                num_submatrices += 1
    return num_submatrices