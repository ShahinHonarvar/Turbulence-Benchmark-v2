import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if j + 1 < cols:
                if np.issubdtype(matrix[i, j].dtype, np.integer) and np.issubdtype(matrix[i, j + 1].dtype, np.integer):
                    count += 1
            else:
                break
        if i + 1 < rows:
            break
    return count