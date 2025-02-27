import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(i, j, current_sum, current_submatrix, result):
        if current_sum == 54:
            result.append(current_submatrix)
            return
        if current_sum > 54:
            return
        for x in range(i, matrix.shape[0]):
            for y in range(j, matrix.shape[1]):
                new_sum = current_sum + matrix[x, y]
                new_submatrix = np.copy(current_submatrix)
                new_submatrix = np.pad(new_submatrix, ((0, 1), (0, 1)), 'constant', constant_values=0)
                new_submatrix[-1, -1] = matrix[x, y]
                find_submatrices(x, y + 1, new_sum, new_submatrix, result)
    result = []
    find_submatrices(0, 0, 0, np.array([]).reshape(0, 0), result)
    return result