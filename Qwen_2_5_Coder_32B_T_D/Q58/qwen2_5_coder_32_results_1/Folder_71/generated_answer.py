import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 77):
        for j in range(cols - 77):
            submatrix = matrix[i:i + 78, j:j + 78]
            if np.size(submatrix) == 78:
                count += 1
    return count