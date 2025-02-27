import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 96
    rows, cols = matrix.shape
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            sub_matrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
            if sub_matrix.size == n:
                count += 1
    return count