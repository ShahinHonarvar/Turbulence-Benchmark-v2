import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, n=47):
        return np.sum(submat == n)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row_size in range(1, rows - i + 1):
                for col_size in range(1, cols - j + 1):
                    submat = matrix[i:i + row_size, j:j + col_size]
                    if count_elements(submat) == 47:
                        count += 1
    return count