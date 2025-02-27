import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submat, target_sum):
        for size in range(1, len(submat) + 1):
            for i in range(len(submat) - size + 1):
                for j in range(len(submat[0]) - size + 1):
                    if np.sum(submat[i:i + size, j:j + size]) == target_sum:
                        return submat[i:i + size, j:j + size]
        return None
    all_submatrices = []
    for rows in range(matrix.shape[0]):
        for cols in range(matrix.shape[1]):
            temp_matrix = matrix[rows:, cols:]
            result = submatrix_sum(temp_matrix, -59)
            if result is not None and (not any((np.array_equal(result, x) for x in all_submatrices))):
                all_submatrices.append(result)
    return all_submatrices