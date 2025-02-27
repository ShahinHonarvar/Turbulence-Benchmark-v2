import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, count):
        flat_list = submat.flatten()
        return len(flat_list) == count
    rows, cols = matrix.shape
    target_count = 20
    count_of_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    if count_elements(matrix[i:r, j:c], target_count):
                        count_of_submatrices += 1
    return count_of_submatrices