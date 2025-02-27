import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, n=99):
        flat_submatrix = submatrix.flatten()
        return np.sum(flat_submatrix == n)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 3 <= rows and j + 3 <= cols:
                submatrix = matrix[i:i + 3, j:j + 3]
                if count_elements(submatrix) == 99:
                    count += 1
    return count