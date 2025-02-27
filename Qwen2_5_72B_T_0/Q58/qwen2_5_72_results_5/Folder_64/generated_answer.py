import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, count):
        flat_list = submat.flatten()
        return flat_list.size == 7 and np.sum(flat_list) == count * 7
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row_end in range(i + 1, rows + 1):
                for col_end in range(j + 1, cols + 1):
                    if count_elements(matrix[i:row_end, j:col_end], 1):
                        count += 1
    return count