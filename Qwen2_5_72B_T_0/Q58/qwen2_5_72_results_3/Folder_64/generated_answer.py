import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, n=7):
        return sum((1 for element in np.nditer(submat) if element == n))
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row_end in range(i + 1, rows + 1):
                for col_end in range(j + 1, cols + 1):
                    submat = matrix[i:row_end, j:col_end]
                    if count_elements(submat) == 7:
                        count += 1
    return count