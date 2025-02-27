import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, n=46):
        return np.sum(submatrix == n)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    if count_elements(matrix[i:x, j:y]) == 46:
                        count += 1
    return count