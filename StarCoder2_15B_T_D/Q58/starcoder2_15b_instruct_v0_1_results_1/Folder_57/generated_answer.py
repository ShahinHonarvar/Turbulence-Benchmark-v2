import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            num_92s = np.count_nonzero(submatrix == 92)
            if num_92s == 92:
                num_submatrices += 1
    return num_submatrices