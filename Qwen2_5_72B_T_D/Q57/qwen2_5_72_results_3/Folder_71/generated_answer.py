import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_sum(i, j, target):
        result = []
        for i_end in range(i + 1, len(matrix) + 1):
            for j_end in range(j + 1, len(matrix[0]) + 1):
                submatrix = matrix[i:i_end, j:j_end]
                if np.sum(submatrix) == target:
                    result.append(submatrix)
        return result
    all_submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            all_submatrices.extend(find_submatrices_sum(i, j, 69))
    return all_submatrices