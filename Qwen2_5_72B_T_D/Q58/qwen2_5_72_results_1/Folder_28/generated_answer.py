import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, n):
        return np.sum(submatrix == n)
    target_count = 37
    rows, cols = matrix.shape
    count_of_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            for width in range(1, cols - j + 1):
                for height in range(1, rows - i + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if count_elements(submatrix, 1) == target_count:
                        count_of_submatrices += 1
    return count_of_submatrices