import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_in_submatrix(submat):
        flat_list = submat.flatten()
        return len(np.unique(flat_list)) == 2
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    if count_in_submatrix(matrix[i:r, j:c]):
                        count += 1
    return count