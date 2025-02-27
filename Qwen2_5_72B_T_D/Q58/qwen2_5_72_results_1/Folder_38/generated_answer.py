import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, target_count):
        flat_list = submat.flatten()
        return len(flat_list) == target_count
    target_count = 34
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row_end in range(i + 1, rows + 1):
                for col_end in range(j + 1, cols + 1):
                    if count_elements(matrix[i:row_end, j:col_end], target_count):
                        count += 1
    return count