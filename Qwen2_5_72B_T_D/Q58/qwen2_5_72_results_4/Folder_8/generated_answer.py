import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, target):
        return np.sum(submat == target)
    target = 29
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                submat = matrix[i:i + size, j:j + size]
                if count_elements(submat, target) == 29:
                    count += 1
    return count