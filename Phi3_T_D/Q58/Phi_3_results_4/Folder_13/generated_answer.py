import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i <= rows - 5 and j <= cols - 5:
                submatrix = matrix[i:i + 5, j:j + 5]
                if np.sum(submatrix) == 175:
                    count += 1
    return count