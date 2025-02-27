import numpy as np

def submatrix_with_n_numbers(matrix):
    target_number = 99
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_number:
                for x in range(i, rows):
                    for y in range(j, cols):
                        if np.sum(matrix[i:x + 1, j:y + 1] == target_number) == 99:
                            submatrix_count += 1
    return submatrix_count