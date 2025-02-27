import numpy as np

def submatrix_with_n_numbers(matrix, n=83):
    count = 0
    rows, cols = (len(matrix), len(matrix[0]))
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                sub_matrix = matrix[i:i + size, j:j + size]
                if np.all(sub_matrix == n):
                    count += 1
    return count