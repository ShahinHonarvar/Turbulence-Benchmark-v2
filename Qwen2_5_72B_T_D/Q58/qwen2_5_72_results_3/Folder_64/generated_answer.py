import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, n=7):
        return np.sum(submatrix == n)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 1 < rows and j + 1 < cols:
                submatrix = matrix[i:i + 2, j:j + 2]
                if count_elements(submatrix) == 7:
                    count += 1
    return count