import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, n=7):
        return np.sum(submatrix == n)
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for row_size in range(1, rows - i + 1):
                for col_size in range(1, cols - j + 1):
                    submatrix = matrix[i:i + row_size, j:j + col_size]
                    if count_elements(submatrix) == 7:
                        count += 1
    return count