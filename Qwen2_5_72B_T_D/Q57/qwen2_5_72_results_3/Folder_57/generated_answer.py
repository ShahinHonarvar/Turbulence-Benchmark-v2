import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(i, j, rows, cols):
        sum_val = 0
        submatrices = []
        for i_end in range(i, rows):
            for j_end in range(j, cols):
                sum_val = np.sum(matrix[i:i_end + 1, j:j_end + 1])
                if sum_val == 13:
                    submatrices.append(matrix[i:i_end + 1, j:j_end + 1])
                elif sum_val > 13:
                    break
        return submatrices
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            result.extend(find_submatrices(i, j, rows, cols))
    return result