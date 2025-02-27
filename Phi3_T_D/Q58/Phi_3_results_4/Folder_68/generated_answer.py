import numpy as np

def submatrix_with_n_numbers(matrix):
    sub_matrices_count = 0
    rows, cols = matrix.shape
    matrix = matrix.flatten()
    for i in range(rows):
        for j in range(cols):
            target_submatrix = np.copy(matrix)
            flat_indices = list(matrix.flat)
            for index in range(i * cols + j, len(flat_indices), cols + 1):
                target_submatrix[index - i * cols] = 0
            if sum((1 for elem in target_submatrix if elem == 74)) == 74:
                sub_matrices_count += 1
    return sub_matrices_count