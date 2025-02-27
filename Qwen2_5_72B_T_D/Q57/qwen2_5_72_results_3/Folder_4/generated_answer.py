import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrix_with_sum(m, target_sum, submatrix_list):
        rows, cols = m.shape
        for i in range(rows):
            for j in range(cols):
                for r_size in range(1, rows - i + 1):
                    for c_size in range(1, cols - j + 1):
                        sub = m[i:i + r_size, j:j + c_size]
                        if np.sum(sub) == target_sum:
                            submatrix_list.append(sub)
        return submatrix_list
    submatrices = []
    target_sum = 87
    return find_submatrix_with_sum(matrix, target_sum, submatrices)