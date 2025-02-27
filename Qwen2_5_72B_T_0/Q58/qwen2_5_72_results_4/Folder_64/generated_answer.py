import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, count):
        flat_list = submat.flatten()
        return flat_list.size == count
    rows, cols = matrix.shape
    target_count = 7
    result = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    if count_elements(matrix[i:r, j:c], target_count):
                        result += 1
    return result