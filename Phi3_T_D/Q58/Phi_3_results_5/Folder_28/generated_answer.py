import numpy as np

def submatrix_with_n_numbers(matrix, n=37):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix of integers')
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.count_nonzero(submatrix == 37) == n:
                        count += 1
    return count