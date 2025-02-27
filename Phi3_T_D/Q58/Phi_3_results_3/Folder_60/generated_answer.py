import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                for r in range(i, rows - size + 1):
                    for c in range(j, cols - size + 1):
                        if (matrix[r:r + size, c:c + size] == np.full((size, size), 88)).all():
                            count += 1
    return count