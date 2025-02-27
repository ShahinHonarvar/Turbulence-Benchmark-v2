import numpy as np

def submatrix_with_n_numbers(matrix, n=21):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n - 1 < rows and j + n - 1 < cols:
                submatrix = matrix[i:i + n, j:j + n]
                if np.unique(submatrix).size == 1:
                    count += 1
    return count