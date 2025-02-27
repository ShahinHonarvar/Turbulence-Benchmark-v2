import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, count):
        return np.sum(submat == count)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            submat = matrix[i:i + 2, j:j + 2]
            if count_elements(submat, 7) == 7:
                count += 1
    return count