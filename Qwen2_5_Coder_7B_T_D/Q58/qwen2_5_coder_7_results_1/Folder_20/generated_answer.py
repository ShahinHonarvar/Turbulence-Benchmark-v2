import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 2 < rows and j + 2 < cols:
                submatrix = matrix[i:i + 3, j:j + 3]
                if np.array_equal(submatrix, np.full((3, 3), 49)):
                    count += 1
    return count