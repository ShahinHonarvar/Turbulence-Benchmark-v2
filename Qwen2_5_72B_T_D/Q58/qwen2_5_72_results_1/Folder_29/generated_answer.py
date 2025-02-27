import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, count):
        flattened = submat.flatten()
        return len(flattened) == count
    rows, cols = matrix.shape
    target_elements = 19
    submatrix_count = 0
    for i in range(rows - target_elements + 1):
        for j in range(cols - target_elements + 1):
            if count_elements(matrix[i:i + target_elements, j:j + target_elements], target_elements):
                submatrix_count += 1
    return submatrix_count