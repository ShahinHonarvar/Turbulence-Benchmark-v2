import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 17
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 3):
        for j in range(cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.sum(submatrix == 17) == target_count:
                count += 1
    return count