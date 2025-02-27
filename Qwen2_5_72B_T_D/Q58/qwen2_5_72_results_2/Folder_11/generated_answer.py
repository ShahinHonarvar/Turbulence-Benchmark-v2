import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, n=38):
        return np.sum(submatrix == n)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row_size in range(1, rows - i + 1):
                for col_size in range(1, cols - j + 1):
                    submatrix = matrix[i:i + row_size, j:j + col_size]
                    if count_elements(submatrix) == 38:
                        count += 1
    return count