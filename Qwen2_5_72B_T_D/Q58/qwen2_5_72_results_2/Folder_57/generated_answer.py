import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_size = 92
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 92:
                for r in range(i, rows):
                    for c in range(j, cols):
                        if (r - i + 1) * (c - j + 1) == target_size:
                            if np.all(matrix[i:r + 1, j:c + 1] == 92):
                                count += 1
    return count