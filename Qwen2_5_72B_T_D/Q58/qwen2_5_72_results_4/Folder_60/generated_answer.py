import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, target):
        return np.sum(submatrix == target)
    target = 88
    required_count = 88
    rows, cols = matrix.shape
    count_of_submatrices = 0
    for i in range(rows - 9 + 1):
        for j in range(cols - 9 + 1):
            submatrix = matrix[i:i + 9, j:j + 9]
            if count_elements(submatrix, target) == required_count:
                count_of_submatrices += 1
    return count_of_submatrices