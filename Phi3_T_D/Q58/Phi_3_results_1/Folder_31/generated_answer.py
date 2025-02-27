import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    if isinstance(matrix, np.ndarray):
        dimensions = matrix.shape
        if 2 <= len(dimensions) <= 3:
            rows, cols = dimensions[-2:]
            for i in range(rows):
                for j in range(cols):
                    for k in range(i, rows):
                        for l in range(j, cols):
                            submatrix = matrix[i:k + 1, j:l + 1]
                            if submatrix.size == 45:
                                count += 1
    return count